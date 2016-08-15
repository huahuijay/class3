#!/usr/bin/python
# -*- coding: utf-8 -*-

import Queue
import threading
import time
import random

num_queue = Queue.Queue()


def ping():
    print threading.current_thread()
    while 1:
        ip = num_queue.get()
        print 'consume:', ip
        time.sleep(1)


def put():
    while 1:
        num = random.randint(1, 1000)
        print 'produce:', num
        num_queue.put(num)
        time.sleep(0.5)


if __name__ == '__main__':
    t = threading.Thread(target=put)
    t.start()

    threads = []
    for i in range(2):
        t = threading.Thread(target=ping)
        t.setName('mythread%s' % i)
        t.setDaemon(True)
        threads.append(t)

    # print 'before start:', threading.activeCount()
    for t in threads:
        t.start()
        t.exit()
         
        # print t.isAlive()
        # print t.isDaemon()

    # print 'after start:', threading.activeCount()
    print 'enumerate', threading.enumerate()
    for t in threads:
        t.join()
