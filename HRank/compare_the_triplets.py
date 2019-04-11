#!/bin/python3


def compareTriplets(a, b):
    _a = 0
    _b = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            _b += 1
        elif a[i] > b[i]:
            _a += 1
    return [_a, _b]

if __name__ == '__main__':
    tests = [
        ([17, 28, 30], [99, 16, 8], '2 1'),
        ([5, 6, 7], [3, 6, 10], '1 1'),
        ([0, 1, 2], [0, 1, 2], '0 0'),
    ]

    for i in tests:
        result = compareTriplets(i[0], i[1])
        assert ' '.join(map(str, result)) == i[2]
