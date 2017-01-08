# From Lorenzo Bolla about GIL
# https://lbolla.info/blog/2013/12/23/python-threads-cython-gil

def busy_sleep(n):
    while n > 0:
        n -= 1


N = 99999999
busy_sleep(N)
busy_sleep(N)
