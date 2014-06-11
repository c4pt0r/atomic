import tornado.web
import router
import time
import json
from views.decorators import check_arguments
from utils import get_global_config, set_global_config
from models.post import Post

@router.route("/")
class IndexViewHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


@router.route("/post")
class TestPostHandler(tornado.web.RequestHandler):
    def get(self):
        p = Post.from_dict({'content':"test"})
        p.save()
        p._content = 'xxxxx'
        p.save()
