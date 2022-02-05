import http.server
import time
import argparse

PORT = 8000

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='delay', type=float, default=0.5,
                        help='Opóźnienie w obsłudze każdego żądania w sekundach')
    args = parser.parse_args()
    delay_time = args.delay

    class DelayServer(http.server.SimpleHTTPRequestHandler):

        def do_GET(self):
            # Generowanie sztucznego opóźnienia dla każdego żądania.
            time.sleep(delay_time)
            super().do_GET()

    Handler = DelayServer

    server = http.server.ThreadingHTTPServer(('localhost', 8000), Handler)
    print('Uruchamianie serwera, użyj <Ctrl-C>, aby zakończyć')
    server.serve_forever()
