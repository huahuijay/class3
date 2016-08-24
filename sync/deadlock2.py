# -*- coding: utf-8 -*-

from threading import Lock
from threading import Thread
import time


def foo(lock1, lock2):
        lock1.acquire()
        time.sleep(1)
        lock2.acquire()

        print 'foo 8888'
        lock2.release()
        lock1.release()


def bar(lock1, lock2):
        lock2.acquire()
        time.sleep(1)
        lock1.acquire()

        print 'bar 8888'
        lock2.release()
        lock1.release()


if __name__ == "__main__":

        lock1 = Lock()
        lock2 = Lock()
        t1 = Thread(target=foo, args=(lock1, lock2))
        t2 = Thread(target=bar, args=(lock1, lock2))

        t1.start()
        t2.start()

        t1.join()
        t2.join()
