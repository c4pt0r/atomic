#encoding=utf-8
import db_utils
import time
from db_utils import init_incr_id
from models import Model, Field

init_incr_id('post')
class Post(Model):
    title = Field("")
    content = Field("")
    channel = Field("")
    create_ts = Field(0)
    view_num = Field(0)
    upvote = Field(0)

init_incr_id('comment')
class Comment(Model):
    uid = Field(-1)
    pid = Field(-1)
    content = Field("")
    create_ts = Field(0)
    upvote = Field(0)
