#!/usr/bin/env python3
"""Serve the reviewed build locally with persistent HTTP/1.1 connections."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class PreviewHandler(SimpleHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

parser = argparse.ArgumentParser()
parser.add_argument('--directory', default='.cache/production-review')
parser.add_argument('--port', type=int, default=1317)
args = parser.parse_args()
directory = Path(args.directory).resolve()
if not (directory / 'index.html').is_file():
    parser.error(f'build index missing: {directory}')
server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(PreviewHandler, directory=str(directory)))
print(f'Preview: http://127.0.0.1:{args.port}/ — {directory}', flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
