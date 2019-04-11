

def staircase(n):
    s = ''
    for i in range(1, n+1):
        s += ('#'*i).rjust(n) + '\n'
    return s


if __name__ == "__main__":
    tests = [
        (1, "#\n"),
        (2, " #\n##\n"),
        (3, "  #\n ##\n###\n"),
        (4, "   #\n  ##\n ###\n####\n"),
    ]
    for i in tests:
        x = staircase(i[0])
        assert x == i[1]
