a=int(input("enter no."))
b=int(input("enter no."))
c=int(input("enter no."))
d=int(input("enter no."))
if a>=b and a>=c and a>=d:
    print(a)
elif b>=c and b>=d and b>=c:
    print(b)
elif c>=d and c>=a and c>=b:
    print(c)
else:
    print(d)