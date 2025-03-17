import cgi
import json
import uuid
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

SERVER_ADDRESS = ('localhost', 8000)
ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'png', 'gif')
ALLOWED_LENGTH = (5 * 1024 * 1024)

class ImageHostingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(open('index.html', 'rb').read())
        else:
            self.send_response(404, 'Not found')

    def do_POST(self):
        # if self.path == '/upload':
        #     content_length = int(self.headers['Content-Length'])
        #
        #     if content_length > ALLOWED_LENGTH:
        #         self.send_response(413, 'Payload Too Large')
        #         return
        #
        #     # filename = self.headers.get('Filename')
        #     print(self.headers)
        #     # print(filename)
        #     # contentdes = self.headers.get('Content-Disposition')
        #     # print(contentdes)
        #
        #     # if not filename:
        #     #     self.send_response(400, 'Lack of Filename header')
        #     #     return
        #
        #     ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
        #     # pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        #     # pdict['CONTENT-LENGTH'] = int(self.headers['Content-Length'])
        #     print(ctype)
        #     print(pdict)
        #
        #     post_data = self.rfile.read(content_length)
        #     print(post_data)
        #
        #     image_id = uuid.uuid4()
        #
        #     with open(f'images/{image_id}.jpg', 'wb') as f:
        #         f.write(post_data)
        #
        #     self.send_response(200)
        #     self.send_header('Content-type', 'text/html; charset=utf-8')
        #     self.end_headers()
        #     self.wfile.write(open('upload_success.html', 'rb').read())
        #
        # else:
        #     self.send_response(405, 'Method Not Allowed')

        if self.path == '/upload':
            content_length = int(self.headers.get('Content-Length'))
            if content_length > ALLOWED_LENGTH:
                self.send_response(413, 'Payload Too Large')
                return

            filename = self.headers.get('Filename')

            if not filename:
                self.send_response(400, 'Lack of Filename header')
                return

            filename, ext = filename.split('\\')[-1].split('.')
            if ext not in ALLOWED_EXTENSIONS:
                self.send_response(400, 'Unsupported file extension')
                return

            data = self.rfile.read(content_length)

            image_id = uuid.uuid4()

            with open(f'images/{image_id}.{ext}', 'wb') as f:
                f.write(data)

            self.send_response(201)
            self.send_header('Location', f'https:{SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}/images/{image_id}.{ext}')
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(open('upload_success.html', 'rb').read())
        else:
            self.send_response(405, 'Method Not Allowed')


def run():
    httpd = HTTPServer(SERVER_ADDRESS, ImageHostingHandler)
    try:
        print(f'Serving at http://{SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}')
        httpd.serve_forever()
    except Exception:
        pass
    finally:
        print('Server stopped')
        httpd.server_close()


if __name__ == "__main__":
    run()