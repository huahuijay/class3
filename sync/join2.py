import threading
import time


class MyThread(threading.Thread):
    def run(self):
        time.sleep(2)
        print '8888'


if __name__ == '__main__':
    t = MyThread()
    t.start()
    t.join()
    print 'main thread end'
