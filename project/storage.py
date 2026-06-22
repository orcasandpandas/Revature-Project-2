import json

def read_data(filepath):
    try:
        f = open(filepath, "r")
        data = json.loads(f.read())
        f.close()
        return data

    except FileNotFoundError:
        return []

def write_data(filepath, data):
    with open (filepath, "w") as write:
        json.dump(data, write)