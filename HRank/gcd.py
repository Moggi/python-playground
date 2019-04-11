import math
import random


def gcd(_a, _b):
    """Returns the Greatest Common Divisor from two integers"""
    while _b:
        _t, _a = _a, _b
        _b = _t % _b
    return _a


if __name__ == "__main__":
    assert gcd(60, 96) == 12
    assert gcd(20, 8) == 4
    for _i in range(20):
        _a, _b = random.randint(10, 100), random.randint(10, 100)
        assert gcd(_a, _b) == math.gcd(_a, _b)
