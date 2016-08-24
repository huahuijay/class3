# -*- coding: utf-8 -*-
import threading
import time
import random

aList = []
event = threading.Event()


class Producer(threading.Thread):
    def run(self):
        while True:
            num = random.randint(0, 1000)
            aList.append(num)
            print 'p before set', num
            event.set()
            event.clear()
            print 'p after clear'
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        while True:
            print 'c before wait'
            print 'c', aList.pop()
            event.wait()
            print 'c after wait'


if __name__ == '__main__':
    p = Producer()
    c = Consumer()

    p.start()
    c.start()

    p.join()
    c.join()
