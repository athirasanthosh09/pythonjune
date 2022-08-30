
while True:
    ch=int(input("1.create\n2.search\n3.remove\n4.replace\nenter your choice-"))
    if ch==1:
        import listmodule
        listmodule.create()
    elif ch==2:
        import listmodule
        listmodule.search()
    elif ch==3:
        import listmodule
        listmodule.remove()
    elif ch==4:
       import listmodule
       listmodule.replace()
    else:
        break

