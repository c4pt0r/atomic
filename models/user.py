#encoding=utf-8
import db_utils
import time
from db_utils import init_incr_id
from models import Model, Field

init_incr_id('user')
class User(Model):
    username = Field("")
    password = Field("")
    email = Field("")

