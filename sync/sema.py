# -*- coding: utf-8 -*-
import threading
import time
import random
import Queue

q = Queue.Queue()


class Producer(threading.Thread):
    def run(self):
        while True:
            print self.getName()
            for i in range(5):
                num = random.randint(0, 1000)
                q.put(num)

            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, sem):
        self.sem = sem
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.sem.acquire()
            if not q.empty():
                print 'c', self.getName(), q.get()
            self.sem.release()
            time.sleep(1)


if __name__ == '__main__':
    sem = threading.Semaphore(5)
    p = Producer()

    c_list = []
    for i in range(10):
        c = Consumer(sem)
        c_list.append(c)

    p.start()
    for c in c_list:
        c.start()

    print 'main', threading.currentThread()
    p.join()
    for c in c_list:
        c.join()
