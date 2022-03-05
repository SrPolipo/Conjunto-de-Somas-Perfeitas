from fastpickle import *
from math import isqrt

primelist = fastload("primelist")
rootdict = fastload("rootdict")
primeset = fastload("primeset")
maxprime = primelist[-1]

def isPrime(n,primeset,maxprime):
    if n > maxprime:
        newprimes(isqrt(n)+1,True)
    if n in primeset:
        return True
    return False

def isPrimeSlow(n,usedprimes):
    for prime in usedprimes:
        if n%prime == 0:
            return False
    return True

def newprimes(root, i=False):
    global primeset
    global primelist
    global rootdict
    usedprimes = set(primelist[:rootdict[isqrt(root)+1]+1])
    newprimes = [n for n in range((root-1)**2, root**2) if isPrimeSlow(n,usedprimes)]
    if i:
        primeset.update(newprimes)
        primelist += newprimes
        rootdict[root] = rootdict[root-1] + len(newprimes)
        fastdump("primeset", primeset)
        fastdump("primelist", primelist)
        fastdump("rootdict", rootdict)
    return None


if __name__ == "__main__":
    print(primelist)
    print(primeset)
    print(rootdict)
