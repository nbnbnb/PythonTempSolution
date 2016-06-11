#!/usr/bin/env python

import threading
from random import randint
from time import sleep
from queue import Queue
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func,args,name=''):
        super().__init__()
        self.name = name  
        self.func = func  
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('start loop','at:',ctime())
        self.res = self.func(*self.args)
        print('loop','done at:',ctime())

def writeQ(queue):
    print('producting object from Q...')
    queue.put('xxx',1)
    print('size now',queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q... size now ',queue.qsize())

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs = [writer,reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i],(q,nloops),funcs[i].__name__)
        threads.append(t)
        
    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

        print(threads[i].getResult())
    

if __name__ == '__main__':
    main()