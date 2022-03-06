from _pickle import load, dump

def fastdump(path, object):
    """
    Faster version of _pickle.dump,
    specifically for this project
    """
    with open(f"Objects/{path}.obj", "wb") as file:
        dump(object, file)

def fastload(path):
    """
    Faster version of _pickle.load,
    specifically for this project
    """
    with open(f"Objects/{path}.obj", "rb") as file:
        return load(file)


if __name__ == "__main__":
    print(primelist:=fastload("primelist"))
    print(primeset:=fastload("primeset"))
    print(rootdict:=fastload("rootdict"))
    print(primelist[rootdict[77]])
