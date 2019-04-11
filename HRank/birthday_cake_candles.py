from collections import Counter


def birthdayCakeCandles(ar):
    """Returns how many candles are the tallest on the cake array"""
    count = Counter(ar)
    tallest = max(ar)
    return count[tallest]


if __name__ == "__main__":
    tests = [
        ([3, 2, 1, 3], 2),
        ([3, 2, 1, 1], 1),
    ]
    for i in tests:
        assert birthdayCakeCandles(i[0]) == i[1]
