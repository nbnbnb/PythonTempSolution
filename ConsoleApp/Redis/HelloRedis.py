#!/usr/bin/python
import time
import redis
import threading

conn = redis.Redis(host='192.168.199.198',port=6379)

def notrans():
    pipeline = conn.pipeline()
    pipeline.incr('trans:')
    time.sleep(0.1)

    pipeline.incr('trans:',-1)
    print(pipeline.execute()[0])


if __name__ == '__main__':
    for i in range(3):
        threading.Thread(target=notrans).start()
    time.sleep(0.5)




