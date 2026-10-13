#!/usr/bin/env python3
"""Check authored metadata and real production HTML targets; external URLs are not fetched."""
import argparse, hashlib, json, re
from pathlib import Path
from urllib.parse import unquote, urlsplit
import yaml
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--public-dir',default='public');args=parser.parse_args()
out=(ROOT/args.public_dir).resolve();errors=[];documents={};ids={};themes=[];draft_urls=[]
def fail(s): errors.append(str(s))
def read(path): return path.read_text(encoding='utf-8')
def permalink(path):
 rel=path.relative_to(ROOT/'content');parts=list(rel.parts)
 if parts[-1]=='_index.md': parts.pop()
 else: parts[-1]=path.stem
 return '/' + ('/'.join(parts) + '/' if parts else '')
seen={};metadata={}
for path in sorted((ROOT/'content').rglob('*.md')):
 text=read(path)
 try: _,front,body=text.split('---',2);meta=yaml.safe_load(front)
 except Exception as e: fail(f'{path}: invalid frontmatter {e}');continue
 for key in ['title','description','page_id','content_kind','scope','status','draft','verified','reviewed_by']:
  if key not in meta: fail(f'{path}: missing {key}')
 metadata[path]=meta
 pid=meta.get('page_id')
 if pid in seen: fail(f'duplicate page_id {pid}: {path} and {seen[pid]}')
 seen[pid]=path
 url=permalink(path)
 if meta.get('draft'):
  draft_urls.append(url)
  if (out/url.lstrip('/')/'index.html').exists(): fail(f'draft leaked: {url}')
  continue
 if meta.get('content_kind') not in ['editorial','concept','task','culture','history','legal','comparison','document','language']: fail(f'{path}: unknown content kind')
 if meta.get('content_kind')!='editorial':
  themes.append((path,meta,body,url))
  if meta.get('status')!='integrated' or not meta.get('verified') or not meta.get('reviewed_by'): fail(f'{path}: public topic has incomplete review metadata')
  if not re.search(r'https?://',body): fail(f'{path}: topic without sources')
 if re.search(r'^# ',body,re.M): fail(f'{path}: repeated h1 in body')
 if re.search(r'|turn\d+(?:search|view)|TODO|待补充',body): fail(f'{path}: internal marker or placeholder')
 stripped=re.sub(r'```.*?```','',body,flags=re.S)
 for m in re.finditer(r'\*\*[^\n]+?\*\*',stripped):
  if re.search(r'[\u4e00-\u9fff]',m.group()):
   if m.start() and not stripped[m.start()-1].isspace(): fail(f'{path}: missing space before Chinese bold')
   if m.end()<len(stripped) and not stripped[m.end()].isspace(): fail(f'{path}: missing space after Chinese bold')
for path in out.rglob('*.html'):
 soup=BeautifulSoup(read(path),'html.parser');documents[path]=soup;ids[path]={tag['id'] for tag in soup.select('[id]')}
 for node in soup.select('a[href],img[src],script[src],link[href]'):
  ref=node.get('href',node.get('src',''));u=urlsplit(ref)
  if u.scheme not in ['', 'http','https'] or u.netloc not in ['', 'us.vonng.com']:continue
  raw=unquote(u.path)
  if not raw: target=path
  elif raw.startswith('/'): target=out/raw.lstrip('/')
  else: target=(path.parent/raw).resolve()
  if target.is_dir():target=target/'index.html'
  if not target.exists():fail(f'{path.relative_to(out)}: missing {ref}')
  elif u.fragment and target.suffix=='.html':
   if target not in ids: ids[target]={n['id'] for n in BeautifulSoup(read(target),'html.parser').select('[id]')}
   if unquote(u.fragment) not in ids[target]:fail(f'{path.relative_to(out)}: missing anchor {ref}')
for path,meta,body,url in themes:
 html=out/url.lstrip('/')/'index.html'
 if html not in documents: fail(f'{path}: HTML not emitted');continue
 soup=documents[html]
 if not soup.select_one('.editorial-meta'):fail(f'{path}: scope not rendered')
 if not (html.parent/'index.md').exists():fail(f'{path}: Markdown source not emitted')
 if len(soup.select('main h1'))!=1:fail(f'{path}: must render one h1')
 if '**' in soup.get_text():fail(f'{path}: unrendered bold marker')
acceptance=ROOT/'ops/reviews/acceptance.json'
if themes:
 if not acceptance.exists():fail('public topics lack acceptance ledger')
 else:
  ledger=json.loads(read(acceptance))
  for path,meta,body,url in themes:
   item=ledger.get(path.relative_to(ROOT).as_posix(),{})
   if item.get('body_sha256')!=hashlib.sha256(body.encode()).hexdigest():fail(f'{path}: review version mismatch')
   if len({item.get('author'),item.get('fact_reviewer'),item.get('static_reviewer')})!=3 or not all(item.get(k) for k in ['author','fact_reviewer','static_reviewer']):fail(f'{path}: three distinct participants required')
   for field in ['fact_record','static_record']:
    if not (ROOT/item.get(field,'missing-record')).is_file(): fail(f'{path}: missing {field}')
def navigation_hidden(path,meta):
 if meta.get('toc_hide'):return True
 for parent in path.parents:
  if parent==ROOT:break
  if metadata.get(parent/'_index.md',{}).get('toc_hide'):return True
 return False
book_doc=documents.get(out/'book/index.html')
if book_doc:
 navrefs={x.get('href') for x in book_doc.select('.us-book-directory a')}
 for path,meta,_,url in themes:
  if (url in navrefs)==navigation_hidden(path,meta):fail(f'directory exclusion/coverage mismatch: {url}')
indexes=list(out.glob('offline-search-index*.json'))
if not indexes:indexes=list(out.rglob('*search*index*.json'))
if not indexes:fail('offline search index missing')
else:
 search=json.loads(read(indexes[0]));refs={x.get('ref') for x in search}
 for path,meta,_,url in themes:
  excluded=navigation_hidden(path,meta) or meta.get('search_exclude')
  if (url in refs)==bool(excluded):fail(f'search exclusion/coverage mismatch: {url}')
 for url in draft_urls:
  if url in refs:fail(f'draft leaked to search: {url}')
 if any('/ops/' in (x or '') for x in refs):fail('ops leaked to search')
print_file=out/'_print/book/index.html'
if not print_file.exists():fail('book print missing')
else:
 soup=documents[print_file]
 for path,meta,_,url in themes:
  excluded=navigation_hidden(path,meta) or meta.get('no_print')
  present=bool(soup.select_one(f'[data-td-book-page="{url.rstrip("/")}"]'))
  if present==bool(excluded):fail(f'print exclusion/coverage mismatch: {url}')
result={'html_files':len(documents),'formal_topics':len(themes),'draft_pages':len(draft_urls),'external_links':'not checked by this script','errors':errors}
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
