# -*- coding: ISO-8859-1 -*-
import thread
import time, random
import threading
from enum import Enum

class Estado(Enum):
    PENSANDO = 0
    FAMINTO = 1
    COMENDO = 2


class Filosofo(threading.Thread):
    def __init__(self, cadeira, mesa):
        threading.Thread.__init__(self)
        self.cadeira = cadeira
        self.mesa = mesa
        print "filosofo %i " % self.cadeira

    def run(self):
        for i in range(random.randint(1, 4)):
            self.pensar()
            self.mesa.pegarGarfo(self.cadeira)
            self.comer()
            self.mesa.largarGarfos(self.cadeira)

    def pensar(self):
        time.sleep(random.randint(3, 10))

    def comer(self):
        time.sleep(random.randint(2, 5))


class Mesa():
    def __init__(self,n):
        self.n = n
        self.estado = list()
        self.mutex = threading.Semaphore(1)

        for i in range(5):
            self.estado.append(Estado.PENSANDO)

    def pegarGarfo(self,cadeira):

        self.mutex.acquire()

        self.estado[cadeira] = Estado.FAMINTO
        print "Filosofo %i esta faminto D:" % cadeira

        self.testar(cadeira)

        self.mutex.release()

    def testar(self, cadeira):

        ESQUERDA = (cadeira+self.n-1) % self.n
        DIREITA = (cadeira+1) % self.n

        if( self.estado[cadeira] == Estado.FAMINTO and
            self.estado[ESQUERDA] != Estado.COMENDO and
            self.estado[DIREITA] != Estado.COMENDO ):

             self.estado[cadeira] = Estado.COMENDO
             print "Filosofo %i comendo!!!" % cadeira


    def largarGarfos(self,cadeira):

        self.mutex.acquire()
        self.estado[cadeira] = Estado.PENSANDO
        print "Filosofo %i esta pensativo..." % cadeira

        self.testar(self.left(cadeira))
        self.testar(self.right(cadeira))
        self.mutex.release()

    def left(self,cadeira):
        esquerda = (cadeira + self.n - 1) % self.n
        return esquerda

    def right(self,cadeira):
        direita = (cadeira + self.n) % self.n
        return direita

    def exit(self,threads):

        t = 0
        while len(threads) > 0:
            i = t % len(threads)

            threads[i].join(1)
            if not threads[i].isAlive():
                print "O filosofo %i se retirou da mesa" % threads[i].cadeira
                threads.remove(threads[i])

            t += 1


n = 5

jantar = Mesa(n)

threads = []
for i in range(n):
    t = Filosofo(cadeira=i,mesa=jantar)
    threads.append(t)
    t.start()

jantar.exit(threads)







#
