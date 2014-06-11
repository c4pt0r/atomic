#encoding=utf-8
import db_utils
import os
from utils import *
try:
    db_utils.init_db(db_utils.db_info_test)
except:
    print "db init error"
    exit(-1)

import tornado.web
import tornado.ioloop
import router
import tornado.autoreload
from views import *
import tornado.httpserver

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="!EAFQ@#$RDASDasdfasdf23412341#!@#!%#@$%",
    debug=True,
)
application = tornado.web.Application(router.route.get_routes(), **settings)

if __name__ == '__main__':
    # start tornado server
    load_config()
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8888)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()
