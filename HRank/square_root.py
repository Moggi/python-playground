
precision = 10e-5


def square_root(x):
    _s, _e = 1, x/2
    m = 0
    while (_e-_s) > precision:
        m = (_e+_s)/2
        if(m*m > x):
            _e = m
        else:
            _s = m
    return m


for _ in range(0, 10+1):
    value = int(input())
    response = square_root(value)
    print(f'{value}: {response:.3f}')
