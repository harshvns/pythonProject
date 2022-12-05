x=int(input("enter no.:"))
y=int(input("enter no.:"))
z=int(input("enter no.:"))
if x>=y and x>=z:
    if y>=z:
        print(y)
    else:
        print(z)
elif y>=x and y>=z:
    if x>=z:
        print(x)
    else:
        print(z)
elif z>=y and z>=x:
    if y>=x:
        print(y)
    else:
        print(x)