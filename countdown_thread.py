# From developerWorks Brasil about threads
# http://imasters.com.br/artigo/20127/py/threads-em-python/?trace=1519021197&source=single

from threading import Thread
import sys
import time

COUNTDOWN = 5


class Th(Thread):

    def __init__(self, num):
        sys.stdout.write("Making thread number " + str(num) + "\n")
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num
        self.countdown = COUNTDOWN

    def run(self):
        while (self.countdown):
            sys.stdout.write(
                "Thread " + str(self.num) + " (" + str(self.countdown) + ")\n"
            )
            sys.stdout.flush()
            time.sleep(.5)  # pretend to do some work.
            self.countdown -= 1


for thread_number in range(60):
    thread = Th(thread_number)
    thread.start()
