import requests
import json

metadata_url = 'http://169.254.169.254/latest/'

def expand_json(url, arr):
    output = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            output[item[:-1]] = expand_json(new_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output

def get_metadata():
    initial = ["meta-data/"]
    result = expand_json(metadata_url, initial)
    return result

def get_metadata_json():
    metadata = get_metadata()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def expand_dict(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in expand_dict(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in expand_dict(key, d):
                        yield result

def find_key(key):
    metadata = get_metadata()
    return list(expand_dict(key, metadata))

if __name__ == '__main__':
    key = input("What would you like to find?\nkey | metadata\n")
    if key=="key":
        key2 = input("Enter the key you need value for?\n")
        print(find_key(key2))
    elif key=="metadata":    
        print(get_metadata_json())
    else: print("Invalid key entered")