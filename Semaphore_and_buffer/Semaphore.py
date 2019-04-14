#A- Reads the file from disk to buffer= one record length
#B- Copy data from buffer1 to buffer2
#C- Take data from buffer2 and print it
#use semaphores for all of these

import threading
import queue


class sharedObject(object):
    def __init__(self, data):
        duffer=queue()
        queue.pop(data)

class readerThread(threading):
    def __init__(self, threadName,data, sem, q):
        self.name = threadName
        self.semaphre = sem
        self.data = data
        self.q = q

    def run():
        with lines in self.data:
            this_line = self.data.readline()
            self.q.pop(this_line)


class copierThread(threading):
    def __init__(self, threadName,data, sem, q):
        self.name=threadName
        self.semaphre=sem
        self.data = data
        self.q = q

    def run():
        print(self.q.pop())


class printerThread(threading):
    def __init__(self, threadName, sem):
        self.name=threadName
        self.semaphre=sem

if __name__ == '__main__'():
    print("*******in the main********")
    Q = queue()
    my_file = open('tset.txt','r')
    collected_data = sharedObject(Q)

    

