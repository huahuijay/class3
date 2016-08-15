#!/usr/bin/python
# -*- coding: utf-8 -*-

import Queue


if __name__ == "__main__":
    q = Queue.Queue(maxsize=5)

    for i in range(6):
        print i
        q.get()

    print 'qsize:', q.qsize()
    print 'is full', q.full()
    print 'is empty', q.empty()
