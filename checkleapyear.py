x=int(input("year:"))
if x%400==0:
    print("leap year")
elif x%100==0:
    print("not leap year")
elif x%4==0:
    print("leap year")