#Hint----> This is an edited version of the last task

import datetime
import threading 

##----------------------OverridingTheThreadClass-------------------------
class mythread (threading.Thread):
    startValue = 0
    endValue = 0
    def __init__(self, val1, val2, name):
        threading.Thread.__init__(self)
        self.name = name
        self.startValue = val1
        self.endValue = val2
    def run(self):
        threadLock.acquire()
        print ("Starting " + self.name)
        calcprime(self.startValue, self.endValue)
        threadLock.release()
        print ("Exiting " + self.name)

##--------------------MainCalculationFunction--------------------------
def calcprime(y,x):
    for n in range(y,x+1):
        count = 0
        if n==2:
            print(n)
        elif n%2==0:
            continue
        else:
            for j in range (1,n+1):
                if n%j==0:
                    count+=1
            if count==2:
                print(n)
                
##--------------------CreatingAndRunningThreads-----------------------------------

x= int(input())
a=int(x/3)
b=int((2*x)/3)

threadLock = threading.Lock()

thread1= mythread(1,a,"firstthread")
thread2= mythread((a+1),b,"secondthread")
thread3= mythread((b+1),(x+1),"thirdthread")

thread1.start()
thread2.start()
thread3.start()
