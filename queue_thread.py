# From sentdex about python3 and queue
# https://youtu.be/NwH0HvMI4EA
# https://pythonprogramming.net/threading-tutorial-python/

import threading
from queue import Queue
import time
import sys

print_lock = threading.Lock()


def exampleJob(worker):
    n = 9999999
    while (n > 0):
        n -= 1
    time.sleep(.5)  # pretend to do some work.
    with print_lock:
        print(threading.current_thread().name, worker)

    # sys.stdout.write(
    #     threading.current_thread().name + " " + str(worker) + "\n")
    # sys.stdout.flush()


# The threader thread pulls an worker from the queue and processes it
def threader():
    while not q.empty():
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        exampleJob(worker)

        # completed with the job
        q.task_done()

# Create the queue and threader
q = Queue()

# 20 jobs assigned.
for worker in range(60):
    q.put(worker)

# how many threads are we going to allow for
for x in range(10):
    t = threading.Thread(target=threader)

    # classifying as a daemon, so they will die when the main dies
    t.daemon = True

    # begins, must come after daemon definition
    t.start()

start = time.time()

# wait until the thread terminates.
q.join()

# with 10 workers and 20 tasks, with each task being .5 seconds, then the
# completed job is ~1 second using threading. Normally 20 tasks with .5 seconds
# each would take 10 seconds.
print('Entire job took:', time.time() - start)
