import os
import json

cfg = {}
cfg_file = os.path.join(os.path.dirname(__file__) + '/conf', "cfg.json")

def set_config_file(fp):
    global cfg_file
    cfg_file = fp

def load_config():
    global cfg
    with open(cfg_file) as fp:
        content = fp.read()
        cfg = json.loads(content)
    return cfg

def dump_config():
    with open(cfg_file, 'w') as fp:
        fp.write(json.dumps(cfg))

def get_global_config(key, default=None):
    return cfg.get(key, default)

def set_global_config(key, value):
    global cfg
    cfg[key] = value
    dump_config()
