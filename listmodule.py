lst=[]
def create():
    n=int(input("enter the number of items:"))
    for i in range(n):
        item=int(input("enter the number "))
        lst.append(item)
    print(lst)

def search():
    n=int(input("enter the number to search:"))
    if n in lst:
        print("found")
    else:
        print("not found")

def remove():
    s=int(input("enter the number to be removed:"))
    if s in lst:
        lst.remove(s)
    else:
        print("not found")
    print(lst)

def replace():
  old=int(input("number to be replaced"))
  new=int(input("number to be added"))
  for i in range(len(lst)):
    if lst[i]==old:
        lst[i]=new
    print(lst)
