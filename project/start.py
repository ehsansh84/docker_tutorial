import os
from copy import deepcopy
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.web import RequestHandler
from data_templates import output

FILE_ROOT = '/www/'
# FILE_ROOT = '/home/oem/www/'


class Upload(RequestHandler):
    def init_method(self):
        self.tokenless = True

    def post(self, *args, **kwargs):
        data = deepcopy(output)
        try:
            file_contents = self.request.files['image'][0]['body']
            file_name = self.request.files['image'][0]['filename']
            if not os.path.exists(FILE_ROOT):
                os.mkdir(FILE_ROOT)
            file = open(FILE_ROOT + file_name, 'wb')
            file.write(file_contents)
            file.close()
        except Exception:
            pass
        self.write(data)



class Test(RequestHandler):
    def init_method(self):
        self.tokenless = True

    def post(self, *args, **kwargs):
        data = deepcopy(output)
        try:
            from pymongo import MongoClient
            # con = MongoClient('localhost:27021')
            con = MongoClient('mongodb://mongo')
            db = con['temp']
            col = db['test']
            import json
            params = json.loads(self.request.body)
            col.insert_one({
                'name': params['name'],
                'family': params['family'],
            })
        except Exception:
            pass
        self.write(data)


url_patterns = [
   ("/v2/upload", Upload, None, "upload_v2"),
   ("/v2/test", Test, None, "test_v2"),

]

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(url_patterns)
    https_app = tornado.httpserver.HTTPServer(app)
    app.listen(8282)
    tornado.ioloop.IOLoop.current().start()
