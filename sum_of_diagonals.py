

def diagonalDifference(arr):
    a = 0
    b = 0
    l = len(arr)
    for i in range(l):
        a += arr[i][i]
        b += arr[l-i-1][i]

    return abs(a-b)

if __name__ == "__main__":
    tests = [
        ([
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ], 15),
        ([
            [1, 2, 1],
            [4, 1, 6],
            [1, 8, 1]
        ], 0),
    ]

    for i in tests:
        assert diagonalDifference(i[0]) == i[1]
