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
            self.condition.acquire()    # 获得条件变量，如果没有获得，那么会阻塞在这里。
            print 'p before acquire'
            num = random.randint(1, 1000)
            print 'p1', num
            q_list.append(num)
            self.condition.notify()
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
            self.condition.acquire()    # 获得条件变量，如果没有获得，那么会阻塞在这里。
            print 'c after acquire'
            print 'c', q_list.pop()
            if not q_list:
                print 'c before wait'
                self.condition.wait()    # 第一次执行的时候，它是阻塞在这里的
                print 'c after wait'
            self.condition.release()
            print 'c after release'


if __name__ == '__main__':
    condition = threading.Condition()
    p = Producer(condition)
    c = Consumer(condition)

    p.start()
    c.start()

    p.join()
    c.join()
