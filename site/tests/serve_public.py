#!/usr/bin/env python3
"""Static file server for the phase suites. The stock
`python -m http.server` died mid-suite twice on 2026-10-23 with the
browser hitting ERR_CONNECTION_REFUSED around the 60 percent mark: its
listen backlog is 5 and it speaks HTTP/1.0, so every asset is a fresh
connection and TIME_WAIT sockets pile up until accept() starts failing.
This server raises the backlog, speaks HTTP/1.1 so the browser reuses
connections, lifts the file-descriptor limit, and restarts its listen
socket instead of dying if serve_forever ever raises. Usage:
serve_public.py PORT DIR
"""
import functools
import resource
import sys
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class Server(ThreadingHTTPServer):
    request_queue_size = 256
    daemon_threads = True
    allow_reuse_address = True


class Handler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    try:
        resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))
    except Exception:
        pass
    port, directory = int(sys.argv[1]), sys.argv[2]
    handler = functools.partial(Handler, directory=directory)
    while True:
        try:
            Server(("127.0.0.1", port), handler).serve_forever()
        except Exception as e:  # last-resort: log and re-listen
            print(f"serve_public: restarting after {e!r}", file=sys.stderr, flush=True)
            time.sleep(0.5)
