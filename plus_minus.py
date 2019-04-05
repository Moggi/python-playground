from collections import Counter


def divide(i):
    if i:
        return i/abs(i)
    return 0


def plus_minus(arr):
    n = len(arr)
    c = Counter({0: 0, 1: 0, -1: 0})
    c.update([divide(i) for i in arr])
    r = list(map(lambda i: round(i/n, 6), [c.get(1), c.get(-1), c.get(0)]))
    return r


if __name__ == "__main__":
    tests = [
        ([-4, 3, -9, 0, 4, 1], [0.500000, 0.333333, 0.166667]),
        ([1, 1, 0, -1, -1], [0.400000, 0.400000, 0.200000]),
        ([0, 0, 0, -0, -0], [0.000000, 0.000000, 1.000000]),
        ([-1, -1], [0.000000, 1.000000, 0.000000]),
        ([1, 1], [1.000000, 0.000000, 0.000000]),
    ]
    for i in tests:
        assert plus_minus(i[0]) == i[1]
