# -*- coding: utf-8 -*-
import time
import threading


def write():
    with open('./data.txt', 'r') as f:
        lines = f.readlines()
        num = int(lines[0].strip('\n'))
        num += 1

    print threading.currentThread(), num
    time.sleep(1)
    with open('./data.txt', 'w') as f:
        f.write(str(num))


if __name__ == '__main__':
    threads = []
    for i in range(2):
        t = threading.Thread(target=write)
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
