import os

def isDict(value):
    return varType(value) == 'dict'

def isList(value):
    return varType(value) == 'list'

def varType(var):
    ss = str(type(var))
    d = ss.split("'")[1]
    #print(d, item)
    return d.strip()

def isFilePresent(filepath):
    return os.path.isfile(filepath)

def isDirectoryCreated(path):
    return os.path.exists(path)

def isDirectoryEmpty(path):
    ln = os.listdir(path)
    return len(ln) > 0