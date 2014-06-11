#encoding=utf-8
import pymongo

db_info_test = {
    'host' : 'localhost',
    'port' : 27017,
    'db'   : 'atomic',
}

con = None
db = None

def init_db(profile):
    global con, db
    con = pymongo.Connection(profile['host'], profile['port'])
    db = con[profile['db']]


def init_incr_id(collection_name):
    if db[collection_name].find_one({'auto_incr_id': {'$exists': True}}) == None:
        db[collection_name].save({'auto_incr_id' : 0})


def gen_incr_id(collection_name):
    id = db[collection_name].find_and_modify(update = {'$inc' : {'auto_incr_id' : 1}}, new = True).get('auto_incr_id')
    return id

def to_dict(o):
    del o['_id']
    return o
