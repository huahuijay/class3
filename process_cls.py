#!/usr/bin/python
# -*- coding: utf-8 -*-


import multiprocessing
import time


class Worker(multiprocessing.Process):
    def run(self):
        while 1:
            # print 'worker'
            # print multiprocessing.current_process()
            time.sleep(1)


if __name__ == '__main__':
    p_list = []
    for i in range(5):
        p = Worker()
        p_list.append(p)

    for p in p_list:
        p.start()

    print 'active process:', multiprocessing.active_children()
    print 'cpu count:', multiprocessing.cpu_count()
    for p in p_list:
        p.join()
