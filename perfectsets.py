from fastpickle import *
import primes


"""
primelist = load(primelist.obj)
 """

class PerfectPower:
    def __init__(self, base, exp):
        self.base = base
        self.exp = exp
    def __repr__(self):
        return f"{self.base}^{self.exp}"

def isPerfectPower(x):
    """
    Checks if a number x is a perfect
    power. If it is returns an object of the
    class PerfectPower, returns False otherwise.
    """
    y = x.bit_length()
    for i in range(2, y + 1, 1):
        min = 1<<((y - 1)//i)
        max = 1<<(y//i + 1)
        mid = (min + max)//2
        while min <= max:
            temp = mid**i
            if temp == x:
                return PerfectPower(mid, i)
            elif temp > x:
                max = mid - 1
            else:
                min = mid + 1
            mid = (min + max)//2
    return False





if __name__ == "__main__":
    print(isPerfectPower(25))
    print(type(isPerfectPower(25)) == PerfectPower)
