# def display():
#     print("welcome")
# def sum():
#     print("sum is:",30+100)
#
#
# student={"name":"athira",
        # "age":23,"mark":30}

# from abc import ABC,abstractmethod
#
# class polygon(ABC):
#
#        @abstractmethod
#        def sides(self):
#            pass
#        def display(self):
#            print("non abstract method")
#
# class  triangle(polygon):
#     def sides(self):
#         print("sum of angles is 180")
#
#
# ob=triangle()
# ob.sides()
# ob.display()


# class human():
#     def say(self,name=None):
#         if name is not None:
#             print("Hello  "+ name)
#         else:
#             print("Hello")
#
# obj=human()
# obj.say()
# obj.say("athira")

# def add(datatype,*args):
#     if datatype=="int":
#         answer=0
#     if datatype=="str":
#         answer=" "
#
#
#     for X in args:
#         answer=answer+X
#     print(answer)
#
#
#
# add("int",4,10)
# add("str","hi ","welcome")

# class rectangle():
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def getarea(self):
#         print(self.length*self.breadth,"is area of rectangle")
#
#
# class square(rectangle):
#     def __init__(self,side):
#         self.side=side
#     def getarea(self):
#         print(self.side*self.side,"is area of square")
#
#
# ob=square(8
#           )
# ob.getarea()
#
#

# class computer():
#     def __init__(self,computer1,ram1,storage1):
#         self.computer2=computer1
#         self.ram2=ram1
#         self.storage2=storage1
#
# class mobile(computer):
#     def __init__(self,computer,ram,storage,model):
#         super().__init__(computer,ram,storage)
#         self.model=model
#
#
#
# obj=mobile("Apple",4,128,"i phone X")
# print("computer is:",obj.computer2)
# print("ram is:",obj.ram2)
# print("storage is:",obj.storage2)
# print("model is:",obj.model)
# l2=[i for  i in range(1,11) if i%2==0]
# print(l2)
# l2=[w for w in "education" if w in["a","e","i","o","u"]]
# print(l2)
# l4=[1,3,5,6,3.6,"sneha ",90]
# l2=[s for s in l4  if type(s)==float]
#print(l2)

# l=[-2,3,-9,7,8,-10]
# d=[x for  x in l if x<0]
# print(d)
# k=["Athira","abhi","css","sneha"]
# l=[fst[0] for fst in k]
'''print(l)'''


#cl=["red","blue","black","green","white"]
# nw=[x for x in cl if "e" in x]
# print(nw)
#nw=[x for x in cl if x!="green"]
# nw=[x.upper() for x in cl ]
#nw=[ "hii" for x in cl]
# l=[x if x!="blue" else "pink" for x in cl]
# print(l)
# t=[lambda a=a:a*10 for a in range(1,11)]
# for i in t:
#     print(i
#           ())