x=int(input("first no."))
y=int(input("second no."))
z=int(input("third no."))
if x>=y and x>=z:
    print("max",x)
elif y>=z:
    print("max",y)
else:
    print("max",z)