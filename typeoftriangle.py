a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a+b<=c or a+c<=b or b+c<=a:
    print("not form triangle")
elif a==b==c:
    print("equilateral")
elif a==b or a==c or b==c:
    print("isosceles")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("right scalene")
else:
    print("scalene")