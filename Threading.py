import time       # time module

def first():               # first function execute every 4sec until condition meet
    n=0
    while(n<=3):
        n+=1
        time.sleep(4)     #timing in sec
        print ("First")
first()    

def second():       #second function execute only after the first function execute even the timing is less then first
    n=0              # In this method we wil not execute function parllel
    while(n<=3):
        n+=1
        time.sleep(2)
        print ("second")
second()

#----------Threading parllel Function execution

import time
import _thread  #thread module  (-thread , start_new_thread(function name,(function argument inside tuple,))) two argument

def first(tex):
    n=0
    while(n<=3):
        n+=1
        time.sleep(4)
        print (tex)
    
def second(tex):
    n=0
    while(n<=3):
        n+=1
        time.sleep(2)
        print (tex)

_thread.start_new_thread(first,("First Function",))   #passing two arguments first function name , second argument of function   
_thread.start_new_thread(second,("Second Function",))  #function argument must be in tuple only

# Multiple threadind with single function

import time
import threading     # threading module (Thread())

def multiple(rang,timing,tex):   #function with three argument (range,time,text)
    for n in range(rang):
        time.sleep(timing)
        print(tex)
first=threading.Thread(target=multiple,args=(3,4,"Multiple threading 1",)) #two argument (target=function name,args=(range,time,text))
first.start()                #start() to start threading
second=threading.Thread(target=multiple,args=(3,2,"Multiple threading 2",)) #two argument (target=function name,args=(range,time,text))
second.start()


