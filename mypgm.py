# class W():
#     def read(self):
#         self.p=int(input("enter the first number:"))
#         self.q=int(input("enter the second number:"))
#
# class X(W):
#     def sum(se):
#         print("sum is :",se.p+se.q)
# class Y(W):
#     def avg(s):
#         print("average is:",(s.p+s.q)/2)
#
# class Z(W):
#     def prod(sl):
#         print("product is:",sl.p*sl.q)
# ob1,ob2,ob3=X(),Y(),Z()
# ob1.read()
# ob1.sum()
# ob2.read()
# ob2.avg()
# ob3.read()
# ob3.prod()

import re
# txt="A beautiful and colourful garden"
# x=re.findall("a",txt)
# print(x)
#
# str ="sat rat pat cat mat 9995 96438 781 87678"
# l=re.findall(r'[spra]',str)
# print(l)
# l1=re.findall(r'[^spr]at',str)
# print(l1)
#
# h=re.findall(r'\b\d{3}',str)
# print(h)

# txt="the rain in spain at 10am"
# x=re.search('sun',txt)
# print(x)
# print(x.start())

# s="The boy is clever"
# d=re.search('^The.*clever$',s)
# if d:
#     print('yes')
# else:
#     print('no')
# str='rose and jasmine are flowers'
# d=re.split('\s''',str)
# print(d)
# str='rose and jasmine are flowers'
# d=re.split('a',str)
# print(d)
# str='rose and jasmine are flowers'
# d=re.split('\s',str,3)
# print(d)
# txt="red and white are colours"
# x=re.sub('\s',' ~ ',txt,2)
# print(x)


# import re
#
# regex = "^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"
#
#
# def check(phone):
#     if (re.search(regex, phone)):
#         print("Valid phone number")
#     else:
#         print("Invalid phone number ")
#
#
# phone ="8921297464"
# check(phone)





# import re
#
# regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
#
#
# def check(pincode):
#     if (re.search(regex, pincode)):
#         print("Valid pincode")
#     else:
#         print("Invalid pincode ")
#         pin ="682005"
# check(pin)


# from queue import LifoQueue
#
# # Initializing a stack
# stack = LifoQueue(maxsize=3)
#
# # qsize() show the number of elements
# # in the stack
# print(stack.qsize())
#
# # put() function to push
# # element in the stack
# stack.put('g')
# stack.put('f')
# stack.put('g')
#
# print("Full: ", stack.full())
# print("Size: ", stack.qsize())
#
# # get() function to pop
# # element from stack in
# # LIFO order
# print('\nElements popped from the stack')
# print(stack.get())
# print(stack.get())
# print(stack.get())
#
# print("\nEmpty: ", stack.empty())

# import queue
#
# # Queue is created as an object 'L'
# L = queue.Queue(maxsize=10)
#
# # Data is inserted in 'L' at the end using put()
# L.put(9)
# L.put(6)
# L.put(7)
# L.put(4)
# # get() takes data from
# # from the head
# # of the Queue
# print(L.get())
# print(L.get())
# print(L.get())
# print(L.get())


# def fib(x):
#     a=0
#     b=1
#     if x<=0:
#         print("in valid")
#     elif x==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,x):
#             c=a+b
#             a=b
#             b=c
#             if(c<=x):
#                 print(c)
# x=int(input("enter the number of values"))
# fib(x)

# Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
# for i, m in enumerate(Months):
#     print(i, m)


# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#         continue
#     print('Current Letter :', letter)
'''from time import sleep
from  threading  import Thread
from time import sleep
from threading import Thread
def task(sleeptime,msg):
     print("wait for a moment")
     sleep(sleeptime)#milliseconds
     print(msg)
 task()
 th=Thread(target=task,args=(2.3,"hai welcome to new msg"))
 th.start()'''

'''import time
import threading

def calsqr(num):
    print("Calculate the square root of given number")
    for n in num:
        time.sleep(.3)
        print("square is:", n*n)
def calcube(num):
    print("calculate cube of given number")
    for n in num:
        time.sleep(.3)
        print('cube is:',n*n*n)
arr=[4,5,6,7,2]
t1=time.time()
th1=threading.Thread(target=calsqr,args=(arr, ))
th2=threading.Thread(target=calcube,args=(arr, ))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken by threads ",time.time()-t1)
'''