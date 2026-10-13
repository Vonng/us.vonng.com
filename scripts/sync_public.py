#!/usr/bin/env python3
"""Synchronize only this project's accepted build and verify paths, bytes and SHA-256."""
import argparse,hashlib,json,shutil
from pathlib import Path
r=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--source',default='.cache/production-review');a=p.parse_args()
s=(r/a.source).resolve();d=r/'public'
if s!=r/'.cache/production-review' or d.resolve()!=r/'public' or s.is_symlink() or d.is_symlink():raise SystemExit('Unexpected build paths')
if not (s/'index.html').is_file():raise SystemExit('Missing reviewed build')
def manifest(base):return {str(f.relative_to(base)):{'size':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in base.rglob('*') if f.is_file()}
before=manifest(s)
# Both exact paths verified above; only stale build files are removed.
if d.exists():
 for f in sorted(d.rglob('*'),reverse=True):
  if f.is_file() and str(f.relative_to(d)) not in before:f.unlink()
  elif f.is_dir() and not any(f.iterdir()):f.rmdir()
shutil.copytree(s,d,dirs_exist_ok=True)
after=manifest(d)
if before!=after:raise SystemExit('Build sync mismatch')
(r/'.cache/public-manifest.json').write_text(json.dumps(after,ensure_ascii=False,indent=2)+'\n')
print(f'Verified {len(after)} paths, file sizes and SHA-256 values')
