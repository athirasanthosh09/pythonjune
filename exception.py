try:
    x=int(input("enter the no1:"))
    y=int(input("enter the no2:"))
    z=x/y
    print(z)

# except ZeroDivisionError as e:
#     print(e)
#
# except ValueError as c:
#     print(c)

except Exception as v:
    print(v)