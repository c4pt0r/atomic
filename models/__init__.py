import json
from db_utils import db, to_dict, gen_incr_id

class Field(object):
    def __init__(self, default):
        self._default = default
    def default(self):
        return self._default

class Model(object):
    def gen_id(self):
        return gen_incr_id(self.table_name())

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        r = {}
        for k in self.__dict__:
            if k.startswith('_'):
                r[k[1:]] = self.__dict__[k]
        return r

    def table_name(self):
        return self.__class__.__name__.lower()

    def save(self):
        if self.id() == None:
            self._id = self.gen_id()
            db[self.table_name()].insert(self.to_dict()) 
        else:
            db[self.table_name()].update({'id': self._id}, {'$set' : self.to_dict()})

    def id(self):
        return self.__dict__.get('_id', None)

    def remove(self):
        if self.id() != None:
            db.posts.remove({'id': self._id})

    @classmethod
    def from_dict(cls, d):
        obj = cls()
        for item in cls.__dict__:
            v = cls.__dict__[item]
            if isinstance(v, Field):
                obj.__setattr__('_' + item, v.default())
        for field in d:
            # ignore mongo's _id
            if field != '_id':
                obj.__setattr__('_' + field, d[field])
        return obj

    @classmethod
    def find(cls, **query):
        return [cls.from_dict(to_dict(res)) for res in db[self.table_name()].find(**query)]
