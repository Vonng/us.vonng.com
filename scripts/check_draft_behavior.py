#!/usr/bin/env python3
"""Exercise independent filtering flags in a fresh isolated source fixture."""
import json,shutil,subprocess
from pathlib import Path
import yaml
from bs4 import BeautifulSoup
r=Path(__file__).resolve().parents[1];f=r/'.cache/draft-fixture';out=f/'output'
if f.is_symlink() or f.resolve()!=r/'.cache/draft-fixture':raise SystemExit('Unexpected fixture path')
if f.exists():shutil.rmtree(f)
f.mkdir(parents=True)
for name in ['content','layouts','assets','data','static']:shutil.copytree(r/name,f/name)
shutil.copy2(r/'hugo.yaml',f/'hugo.yaml');(f/'themes').symlink_to(r/'themes',target_is_directory=True)
probes={'draft':{'draft':True,'status':'written'},'hidden':{'toc_hide':True},'search-only':{'search_exclude':True},'print-only':{'no_print':True},'status-only':{'status':'written'}}
for name,attrs in probes.items():
 data={'title':f'FILTER_PROBE_{name}','description':'Filtering fixture','page_id':f'probe.{name}','content_kind':'concept','scope':'Fixture only','draft':False,'status':'integrated',**attrs}
 (f/f'content/book/probe-{name}.md').write_text('---\n'+yaml.safe_dump(data)+'---\n\nFILTER_PROBE_BODY_'+name+'\n')
nested=f/'content/book/probe-draft-chapter/page.md';nested.parent.mkdir();nested.write_text('---\ntitle: FILTER_PROBE_NESTED\ndraft: true\n---\n\nNESTED_DRAFT_BODY\n')
hidden=f/'content/book/probe-hidden-parent';hidden.mkdir()
(hidden/'_index.md').write_text('---\ntitle: FILTER_PROBE_PARENT\ntoc_hide: true\n---\n\nHIDDEN_PARENT_BODY\n')
(hidden/'child.md').write_text('---\ntitle: FILTER_PROBE_CHILD\n---\n\nHIDDEN_CHILD_BODY\n')
subprocess.run(['hugo','--source',str(f),'--destination',str(out),'--environment','production','--cleanDestinationDir','--panicOnWarning'],check=True,capture_output=True,text=True)
idx=json.loads(next(out.glob('offline-search-index*.json')).read_text());refs={x['ref'] for x in idx}
pr=(out/'_print/book/index.html').read_text();book=BeautifulSoup((out/'book/index.html').read_text(),'html.parser')
nav={a.get('href') for a in book.select('.us-book-directory a,.td-shell-sidebar a')}
assert not (out/'book/probe-draft/index.html').exists()
assert not (out/'book/probe-draft-chapter/index.html').exists(), 'Empty section leaked from nested draft'
assert '/book/probe-draft/' not in refs and 'FILTER_PROBE_draft' not in pr
for route,marker in [('probe-hidden','FILTER_PROBE_hidden'),('probe-hidden-parent','FILTER_PROBE_PARENT'),('probe-hidden-parent/child','FILTER_PROBE_CHILD')]:
 assert (out/f'book/{route}/index.html').exists()
 assert f'/book/{route}/' not in refs and f'/book/{route}/' not in nav and marker not in pr, route
assert '/book/probe-search-only/' not in refs and '/book/probe-search-only/' in nav and 'FILTER_PROBE_BODY_search-only' in pr
assert '/book/probe-print-only/' in refs and '/book/probe-print-only/' in nav and 'FILTER_PROBE_BODY_print-only' not in pr
assert (out/'book/probe-status-only/index.html').exists(), 'Hugo behavior changed; review workflow gate'
report={'draft':'excluded from HTML/search/print; draft-only chapter absent','toc_hide':'leaf and whole ancestor subtree excluded from search/nav/print; direct HTML remains','search_exclude':'search only','no_print':'print only','status_only':'Hugo emits written + draft:false; project metadata checker is required','fixture':str(f)}
(r/'.cache/draft-behavior.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
