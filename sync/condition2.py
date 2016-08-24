# -*- coding: utf-8 -*-
import random
import time
import threading


q_list = []


class Producer(threading.Thread):
    def __init__(self, condition):
        threading.Thread.__init__(self)
        self.condition = condition

    def run(self):
        while True:
            print 'p before acquire'
            self.condition.acquire()
            for i in range(3):
                num = random.randint(1, 1000)
                print 'p1', num
                q_list.append(num)
            # self.condition.notify()
            self.condition.notifyAll()
            print 'p after notify'
            self.condition.release()
            print 'p after release'
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, condition):
        threading.Thread.__init__(self)
        self.condition = condition

    def run(self):
        while True:
            print 'c before acquire'
            self.condition.acquire()
            print 'c after acquire'
            if q_list:
                print q_list.pop()
            if not q_list:
                print 'c before wait'
                self.condition.wait()
                print 'c after wait', self.getName()
            self.condition.release()
            print 'c after release'


if __name__ == '__main__':
    condition = threading.Condition()
    p = Producer(condition)
    c_list = []
    for i in range(3):
        c = Consumer(condition)
        c_list.append(c)

    p.start()
    for c in c_list:
        c.start()

    p.join()
    for c in c_list:
        c.join()
