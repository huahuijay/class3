# -*- coding: utf-8 -*-
import time
import threading


def write(lock):
    lock.acquire()
    with open('./data.txt', 'r') as f:
        lines = f.readlines()
        num = int(lines[0].strip('\n'))
        num += 1

    print threading.currentThread(), num
    time.sleep(1)
    with open('./data.txt', 'w') as f:
        f.write(str(num))
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    threads = []
    for i in range(2):
        t = threading.Thread(target=write, args=(lock,))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
