# import pymysql
# dbcon=pymysql.connect(host='localhost',user='root',password='0914python',database='june')
# cobj=dbcon.cursor()

# idemp=int(input("Enter the id:"))
# name=input("Enter the name")
# salary=int(input("enter the salary:"))
#sql="insert into emp values(%s,%s,%s)"
# val=(idemp,name,salary)
#cobj.execute(sql,val)
# dbcon.commit()
# print("Inserted Succesfully")

# sal=int(input("enter salary"))
# id=int(input("enter the id"))
# sql="update emp set salary='%s' where idemp='%s'"%(sal,id)
# cobj.execute(sql)
# dbcon.commit()

# id=int(input("enter id-"))
# sql="select * from emp where idemp=%d"%id
# cobj.execute(sql)
# i=cobj.fetchone()
# print("id=",i[0])
# print("name=",i[1])
# print("salary=",i[2])

# sql="select * from emp"
# cobj.execute(sql)
# alldata=cobj.fetchall()
# for i in alldata:
#     print("id=",i[0])
#     print("Name=",i[1])
#     print("Salary=",i[2])

# id=int(input("enter id"))
# sql="delete from emp where idemp=%d"%id
# cobj.execute(sql)
# dbcon.commit()
# print("deleted succesfully")


# n=int(input("enter the numbr of row"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# s: store sum of all numbers
# s = 0
# n = int(input("Enter number "))
# # run loop n times
# # stop: n+1 (because range never include stop number in result)
# for i in range(1, n + 1, 1):
#     # add current number to sum variable
#     s += i
# # print("\n")
# print("Sum is: ", s)


n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)


