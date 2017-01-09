# From Lorenzo Bolla about GIL
# https://lbolla.info/blog/2013/12/23/python-threads-cython-gil

from multiprocessing import Process


def busy_sleep(n):
    while n > 0:
        n -= 1


N = 99999999
t1 = Process(target=busy_sleep, args=(N, ))
t2 = Process(target=busy_sleep, args=(N, ))
t1.start()
t2.start()
t1.join()
t2.join()
