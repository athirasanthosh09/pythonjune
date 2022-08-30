# d=10
# print(type(d))
# s="hai"
# print(type(s))
# a=90.5
# print(type(a))
# c=34j
# print(type(c))
# b=False
# print(type(b))
# l=[1,2,3,4,5]
# print(type(l))
# sl=["red",'green',"white"]
# print(type(sl))
# dt=["red",100,5]
# print(type(dt))
# st={5,6,7,23}
# print(type(st))
# tp=("cpp","java","c#","python")
# print(type(tp))
# dc={1:"anu",2:"athira"}
# print(type(dc))
#
# n=int(input("limit:"))
# a,b=0,1
# print(a)
# print(b)
# for i in range(3,n+1):
#     c=a+b
#     print(c)
#     if i%n==0
#      print("false")
#      else
# t="welcome*to*ootty*nice*to*meet*you"
# t=t.split('*')
# print(t)

# p=100
# q=100
# print(p is q)
# p=[100]
# q=[100]
# print(p is q)
#
# p=100
# q=100
# print(p == q)
# p=[100]
# q=[100]
#print(p==q)

# class student:
#     name="athira"
#
# obj=student()
# print(obj.name)
# class A:
#     def display(self):
#         print("simple function")
#     def sum(s,a,b):
#         print("sum is:",a+b)
#
# obj=A()
# obj.display()
# obj.sum(100
#         ,200)

# class fact:
#     def factorial(s,n):
#         f=1
#         for x in range(1,n+1):
#            f=f*x
#         print("factorial is:",f)
#
# #n=int(input("enter a number:"))
# obj=fact()
# obj.factorial(5)

#constructor
# class student():
#     def __init__(self,name):
#         print("name is :",name)
#
# obj=student("athira")

# class student():
#     def __init__(self,name,dep):
#         self.nm=name
#         self.d=dep
#         print("name is:",self.nm)
#         # print("department is",self.d)
#     def display(self):
#         print("Name :", self.nm)
#         print("Department :", self.d)
# obj=student("athira","BCA")
# obj.display()
#
# class student():
#     def __init__(se,name,addr):
#         se.nm=name
#         se.ad=addr
#     def display(x):
#         print("name ",x.nm)
#         print("address",x.ad)
#
# obj=student("athira","Ernakulam")
# obj.display()
# print("name is:", obj.nm)
# print("address is", obj.ad)
#
# obj.ad="kochi"
# print("address is",obj.ad)
# obj.display()

# class student():
#     c=0
#     def __init__(self):
#         student.c=student.c+1
#
#
# obj1=student()
# obj2=student()
# obj3=student()
# print("count=",student.c)

# class product():
#     p=1
#     def __init__(se,n1,n2):
#         se.n=n1
#         se.m=n2
#
#     def display(self):
#         print("product is",self.n * self.m)
#
#
# s=int(input("enter a number:"))
# q=int(input("enter a number:"))
# obj=product(s,q)
# obj.display()
#
#
# class person:
#     def __init__(self):
#         self.name="athira"
#     def display(self):
#         print("Name is:",self.name)
#     class dob:
#         def __init__(self):
#             self.dd=9
#             self.mm=9
#             self.yy=2001
#         def display(self):
#             print("dob is :{}/{}/{}".format(self.dd,self.mm,self.yy))
#
#
# obj=person()
# obj.display()
# obj1=obj.dob()
# obj1.display()
#
# class student:
#     def __init__(self):
#         print("object is created")
#     def __del__(self):
#         print("object is deleted")
#
# obj4=student()
# del obj4

# class A:
#     def displayA(self):
#         print("base class method")
# class B(A):
#     def displayB(self):
#         print("derive class method")
#
# obj=B()
# obj.displayA()
# obj.displayB()
#
# class A:
#     def read(self):
#         self.s = int(input("enter a number1:"))
#         self.q = int(input("enter a number2"))
#
# class B(A):
#     def sum(sel):
#         print("sum is:",sel.s+sel.q)
#
#
#
# obj=B()
# obj.read()
# obj.sum()

# class A:
#     def personaldata(self):
#         self.name = input("enter a name:")
#         self.age = int(input("enter a age:"))
#         self.phone= int(input("enter a phone number:"))
#
#
# class B:
#     def educationalbackground(sel):
#         sel.quali= input("enter the qualification")
#         sel.mark=input("enter mark")
#         sel.univ=input("enter university")
# class C(A,B):
#     def Student(s):
#         print("\t~~Student Details~~\t")
#         print("\t************\t")
#         print("\tname:\t",s.name)
#         print("\tage:\t", s.age)
#         print("\tphone:\t", s.phone)
#         print("\tqualification:\t", s.quali)
#         print("\tmarks:\t", s.mark)
#         print("\tUniversity Name:\t", s.univ)
#
# obj=C()
# obj.personaldata()
# obj.educationalbackground()
# obj.Student()


#print('{2} {1} {0}'.format('directions','the','read'))
#name='john'
#age=23
# print("%s is %d years old"%(name,age))
#print(f'{name} is {age} years old')
# x=12
# print("variable as interger = %d\n variable as float = %f"%(x,x))

# n=123.98
# print("numb is{0:.2f}".format(n))


# p=float8=(12.7)
# q=float('9.9')
# print('{},{}'.format(p,q))


# words= ["Apple", "Banana", "Car", "Dolphin" ]
# for word in words:
#         #This loop is fetching word from the list
#         print (f"The following lines will print each letters of {word}")
#         for letter in word:
#                 #This loop is fetching letter for the word
#                 print (letter)
# nums = [1, 2, 3, 4, 5, 6]
# n = 9
# found = False
# for num in nums:
#     if n == num:
#         found = True
#         break
#
# print(f'List  {n}: {found}')
# num=(1,3,5,7)
# s=0
# for n in num:
#     s=s+n
# print(f"sum of numbers is {s}")
# s=[1,-9,3,8,-7]
# pos=0
# for i in s:
#     if i>0:
#         pos=pos+i
#         continue
# print(f"positive numbers {pos}")


# s=[1,-9,3,8,-7]
# pos=0
# for i in s:
#     if i>=0:
#         print(i)#only positive numbers
# n=int(input("enter limit:"))
# print("odd numbers")
# i=1
# while i<=n:
#     if i%2==1:
#         print(i)
  #i=i+1
# Python 3.x program to check if an array consists

def contains_even_number(l):
	for ele in l:
		if ele % 2 == 0:
			print ("list contains an even number")
			break

	# This else executes only if break is NEVER
	# reached and loop terminated after all iterations.
	else:
		print ("list does not contain an even number")

# Driver code
print ("For List 1:")
contains_even_number([1, 9, 8])
print (" \nFor List 2:")
contains_even_number([1, 3, 5])







