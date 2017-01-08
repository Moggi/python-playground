# From Lorenzo Bolla about GIL
# https://lbolla.info/blog/2013/12/23/python-threads-cython-gil

from threading import Thread


def busy_sleep(n):
    while n > 0:
        n -= 1


N = 99999999
t1 = Thread(target=busy_sleep, args=(N, ))
t2 = Thread(target=busy_sleep, args=(N, ))
t1.start()
t2.start()
t1.join()
t2.join()
