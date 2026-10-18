"""HTTP server with COOP/COEP headers for SharedArrayBuffer support"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import sys
from pathlib import Path

class HeaderHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    directory = sys.argv[2] if len(sys.argv) > 2 else 'public'
    
    import os
    os.chdir(Path(__file__).parent)
    
    server = ThreadingHTTPServer(('127.0.0.1', port), 
                                  lambda *args: HeaderHandler(*args, directory=directory))
    print(f'Server with COOP/COEP headers running at http://localhost:{port}/')
    print('Press Ctrl+C to stop')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped')
        server.server_close()
