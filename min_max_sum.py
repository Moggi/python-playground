

def minMaxSum(arr):
    arr = sorted(arr)
    mi = sum(arr[:-1])
    ma = sum(arr[1:])
    return mi, ma


def miniMaxSum(arr):
    print(*minMaxSum(arr))


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 10, 14),
        ([2, 2, 3, 4, 4], 11, 13),
    ]
    for i in tests:
        assert minMaxSum(i[0]) == (i[1], i[2])
        miniMaxSum(i[0])
