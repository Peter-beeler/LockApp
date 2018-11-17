import json
def load_config():
    f = open('config.json', 'r')
    the_config = json.load(f)
    f.close()
    return the_config