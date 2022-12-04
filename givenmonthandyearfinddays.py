m=int(input("enter month:"))
y=int(input("enter year:"))
if y%400==0 and m==2:
    print("29 days")
elif y%100==0 and m==2:
    print("28 days")
elif y%4==0 and m==2:
    print("29 days")
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("31 days")
elif m==4 or m==6 or m==9 or m==11:
    print("30 days")