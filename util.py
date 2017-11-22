import config
import json

def read(filename, is_json=False):
    with open(filename) as file:
        if is_json:
            return json.loads(file.read())
        return file.read()

def load_constructor():
    return read(config.constructor, is_json=True)
