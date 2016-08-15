#!/usr/bin/python
# -*- coding: utf-8 -*-

import Queue
import threading
import time

ip_queue = Queue.Queue()


class Ping(object):
    def __call__(self):
        while 1:
            if not ip_queue.qsize():
                break
            ip = ip_queue.get()
            time.sleep(1)
            print ip


if __name__ == '__main__':
    for i in range(254):
        ip = '192.168.1.%s' % (i + 1)
        ip_queue.put(ip)

    threads = []
    for i in range(50):
        t = threading.Thread(target=Ping())
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
