# print('{0}, {1} ,{2}'. format(3,7,9))
# name= "john"
# age= 23
# salary= 23500
# print(f'{name} is {age} years old with salary {salary} ')
# mylist=[1,2,3]
# print("A list: %s" %mylist)
# z=5+3j
# print("real ={0} and imaginary={1}". format(z.real,z.imag))
# n=123.987
# print("number is {0:.1f}".format(n))
# a=int(input("enter the number:"))
# if a>0:
#     print("The given number is positive")
# elif a<0:
#     print("The given number is negative")
#   else:
#     print("The given number is zero")
# n1=int(input("Enter the first number"))
# n2=int(input("Enter the second number"))
# op=input("Enter the operator")
# if op=='+':
#     print("sum is:",n1+n2)
# elif op == '-':
#     print("difference is:", n1 - n2)
# elif op=='*':
#     print("product is",n1*n2)
# elif op=="/":
#     print("quotient is",n1/n2)
# elif op=='%':
#     print("remainder is",n1%n2)
# else:
 #print("invalid operation")

# a=int(input("Enter a number:"))
# rev=0
# while a>0:
#     rm=a%10
#     rev=rev*10+rm
#     a=a//10  #floordivision
# print("reverse is:",rev)
# n1=int(input("enter a number:"))
# rev=0
# m=n1
# while n1>0:
#     rm=n1%10
#     pr=rm*rm
#     n1=n1//10
# f m==rev:
#         print("The Number  is Pallindrome" ,rev)
# else:
#         print(" Not a pallindrome",rev)
# str=input("Enter a string:")
# rev=""
# m=str
# count=len(str)
# while count>0:
#     rev=rev+str[count-1]
#     count=count-1
# if m==rev:
#     print("given string is pallindrome ,",rev )
# else:
#     print("given string is not a pallindrome,",rev)

# n=int(input("Enter a number"))
# r=1
# while n>0:
#    s=n%10
#    r=r*s
#    n=n//10
# print("product :",r)
# n1=int(input("enter the number"))
# z=0
# b=n1
# while n1>0:
#     c=n1%10
#     z=z+c*c*c
#     n1=n1//10
# if b==z:
#     print("It is an armstrong number")
#  else:
#     print("it is  not an armstrong number")



# n=int(input("Enter the number"))
# f=0
# for i in range(1,n+1):
#   if n%i==0:
#       f=f+1
# if f==2:
#     print("it is a prime number")
# # else:
#     print("not a prime")
# l1=['anu','asha','diya']
# l2=[100,200,300]
# for i in l1:
#     for j in l2:
#         print(i,j)
# n=int(input("enter the number"))
# print("prime numbers:")
# f=0
# for i in range(2,n+1):
#     j=2
#     for j in range(2,i+1):
#         if(n%j==0):
#             i=j
#         f=f+1
# if f==2:
#         print("it is a prime number")
# else:
#         print("not a number")
# print(n)

#
# n=int(input("enter the number of rows:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j,end=' ')
#
#     print()
#     for i in range(n,0,-1):
#             for j in range(1,i+1):
#                 print(j,end=' ')
#
#             print()

# n=int(input("Enter the number of rows "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j*i,end=' ')
#     print()

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#         for s in range(n-i):
#             print(" ",end=' ')
#         for j in range(1,i+1):
#             print(j,end=' ')
#         for j in range(i-1,0,-1):
#             print(j,end=' ')
#
#         print()
#
# str="Good morning"
# s1=slice(-1,-
# 8,-2)
# print(str[s1])
# str="welcome"
# print(str[::-1])
# n=int(input("Enter the ascii number:"))
# for i in range(5):
#     for j in range(5):
#         if i+j==2 or i-j==2 or i+j==6 or j-i==2:
#             print("*",end=' ')
#         else:
#             print(end=' ')
# print()
#
# ascii_number=65
# rows=7
# for i in range(0,rows):
#     for j in range(0,i+1):
#         character=chr(ascii_number)
#         print(character,end=' ')
#         ascii_number +=1
#     print()
# w="wonderful"
# x=" "
# for i in w:
#     x+=i
#     print(x)
# lst=['green','blue','red','white','yellow','pink','red']
# print(lst[2:5])
# print(lst[4:])
# print(lst[:3])
# print(lst[-5:-1])
# lst[2]='orange'
# print(lst)
# if 'pink' in lst:
#     print("found")
# else:
#     print("not found")
# print('length is:',len(lst))
# lst.append('rose')
# print(lst)
# lst.insert(2,'yellow')
# print(lst)
#lst=['red','green','white','red']
#lst.remove('red')#mutilple itemif occurs first one wll be removed
#lst.remove('white')
#lst.pop()#last item will be poped
#print(lst)
#lst.clear()
#print(lst)
# l1=[1,2,3,4,5]
# l2=(6,7,8,9,10)
# l1.append(l2)
#print(l1)
# print(l1[5])
#print(l1[5][2])
#l1[5].append(777)
#print(l1)
#l1[5].insert(2,99)
#print(l1)
# l3=[100,2,33,99,1,3,200,39,48]
# l3.sort(reverse=True)
# print(l3)
# l4=['red','green','black','grey','blue','maroon','white','purple']
# l4.sort()
# print(l4)
#l1=[1,2,3,4,5]
# l2=l1.copy()
# print(l2)
# l3=[9,8]
# l3=l1.copy()
# print(l3)
#print((sum(l1)))
# lst=[]
# n=int(input("Enter the limit:"))
# for i in range(1,n+1):
#     i**=2
#     lst.append(i)
# print(lst)
# lst1=[2,3,4]
# lst2=[5,6,7]
# print(lst1+lst2)
# lst=[11,2,3,4,25,6,7,8,9]
# print(max(lst))
# lst=[1,2,3,4,5,6,7,89]
# max=lst[0]
# for i in range(len(lst)):
#     if lst[i]>max:
#         max=lst[i]
# print("greater is:",max)
# s=["violet","green","cyan"]
# print(max(s))
# print(min(s))
# L=[[1,2],[3,4],[5,6]]
#print(L[-1])
# def fullname(na1,na2):
#     fna=na1+' '+na2
#     return fna
#
# fna=input("enter the firstname:")
# lna=input("enter the lastname:")
# newname=fullname(fna,lna)
# print(newname)
# def sum():
#     s=n1+n2
#     return s
# n1=int(input("enter the number"))
# n2=int(input("enter the number"))
# print(n1+n2)

# def check():
#     return True

# if check():
#     print("yes True")
# else:
#     print("no false")
#
#print(check())
# x=check()
# print(x)

# def factorial(fac):
#
#     for i in range(1,fac+1):
#         f=f*i
#         return f
# s= int(input("enter the number:"))
# x=factorial(s)
# print(x)

"""def fact(n1):
    if n1==1:
        return 1
    else:
        return(n1*fact(n1-1))
#
n=int(input("enter the number:"))
if n<0:
    print("not exist")
elif n==0:
    print("zero")
else:
    z=fact(n)
    print("factorial is",z)"""
# def display(*args):
#     for i in args:
#         print(i)
# display(10,203,30,45)
# def display(*args):
#     print("last number is",args[1])
#
# display(1,2,3)

"""def display(num1,*args):
    for i in args:
    

        print(i)
    print("first number is",num1)

display(12,23,45,)"""
"""def sum(n1,n2):
    p=n1+n2
    return p


r=int(input("enter:"))
s=int(input("enter:"))
res=sum(r,s)
print(res)"""
# def func(e):
#     return e
#
#
# cars = ['ford','swift','BMW','volvo','nano']
# cars.sort()
# print(cars)
# s=dict(name='athira',age=20,country='India')
# print(s)
# lst=[1,2,3,4,5]
# lst.reverse()
# print(lst)
# seqTuple=('g','r','e','e','n')
# print(list(reversed(seqTuple)))
"""s=bin(6)
print(s)"""
# x=round(4.7896,2)
# print(x)
# c=[4,5,6,4,7,8]
# d=c.index(7)
# e=c.index(4)
# print(d)
# print(e)
"""x=abs(3+4j)
print(x)"""
# p=bool(4)
# print(p)
# m=[0,0.0,0.00,0.1]
# x=any(m)
# print(x)
# s=list(('appple',"banana",'mango'))
# print(s)
# z=isinstance("hello", (float,dict,str))
# print(z)
# x=ascii("¥")
# print(x)
# a=ascii("å")
#print(a)
# def display(**kwargs):
#     for i,j in kwargs.items():
#
#         print('%s==%s'%(i,j))
#
#
# display(c1="riya",c3="abhi",c2="anu")
"""def display(arg,*args,**kwargs):
    print("normal argumnnt",arg)
    print("arbitrary arguments")
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print('%s==%s'%(k,v))


display("keerthana","kiran","anu",c1="diya",c3="abhi",c2="vimal")"""
# def display(a1,a2,a3):
#     print("a=",a1)
#     print("b=",a2)
#     print("c=",a3)
#
#
# x={'a1':'python',"a2":"cpp","a3":"java"}
# display(**x)
# def display(language="python"):
#     print("our language:",language)
#
# display(".net")
# display()
# def display(l1):
#     for i in l1:
#         print(i)
#
#
# l=['rose','jasmine','sunflower']
# display(l)
#
# x=100 #//globalvariable
# y=800
# def check():
#     x=200
#     global z
#     z=500
#     print("inside value of x:",x)
#     #print("inside value of y:", y)
#     print("inside value of z:", z)
#
# check()
# print("outside value of x:",x)
# print("outside value of z:",z)
# l1=[1,2,3,4]
# l2=[1,4,9,16]
# outputlist=list(zip(l1,l2))
# print(outputlist)
#
# outputdict=dict(zip(l1,l2))
# print(outputdict)

#    print('%s has %d years old and lives in %s'%(n,ag,adrs))




# f=open("data.txt","w")
# f.write("python is a trending language")
# f.close()
#
# f= open("data.txt","r")
# print(f.read())
#

# f=open("data.txt","r")
# f.seek(10)
# print(f.read())
#
# f=open("data.txt","r")
# l=f.readline()
# position=f.tell()
# print("position is:",position)
# f.close()


# def test(fname):
#     with open(fname) as f:
#         contents=f.readlines()
#         print(contents)
#
#
#
# test("data.txt")
# from shutil import copyfile
# copyfile("data.txt","destination.txt")

# days={"mon","tues","wed"}
# print(list(enumerate(days)))
#
# print(list(enumerate(days,5)))

# def file_length(fn):
#      with open(fn) as f:
#         for index,value in enumerate(f,1):
#             pass
#         return indexe
#
# print("length:",file_length("data.txt"))


# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def display(self):
#         print(self.name)
#         print(self.__age)
#
# ob=A("kiran",33)
# ob.display()
# print(ob.name)
# print(ob._A__age)

# stack=[]
# stack.append("h")
# stack.append("j")
# stack.append("h")
# print(stack)
# print("\n elements popped from stack")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
#
# print("\nstack after elements are popped")
# print(stack)

# queue = []
#
# # Adding elements to the queue
# queue.append('g')
# queue.append('f')
# queue.append('g')
#
# print("Initial queue")
# print(queue)
#
# # Removing elements from the queue
# print("\nElements dequeued from queue")
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
#
# print("\nQueue after removing elements")
# print(queue)




