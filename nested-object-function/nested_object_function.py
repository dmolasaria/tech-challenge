import json

object = input("Please enter object as dictionary\n")
print("You entered: " + object)
convertedToDict = json.loads(object)

key = input("Please enter key\n")
print("You entered: " + key)

key_length = len(key.split("/"))
key = key.split("/")[key_length-1]

jdata = (json.loads(json.dumps(convertedToDict)))

def dict_get(x,key,here=None):
    if here is None: here = []
    if x.get(key):
        here.append(x.get(key))
        x.pop(key)
    else:
        for i,j in x.items():
          if  isinstance(x[i],list): dict_get(x[i][0],key,here)
          if  isinstance(x[i],dict): dict_get(x[i],key,here)
    return here

value = dict_get(jdata,key)
print(value[0])