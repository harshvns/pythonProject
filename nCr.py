n = 4
r = 0
# 5x6/(2)
coeff=[]
r=(n+1)//2
while (r <= n):
    a = 1
    n1, n2 = r, n - r
    if n1 < n2:
        n1, n2 = n2, n1
    # print(n1, n2)
    num = 1
    for i in range(n1 + 1, n + 1):
        num *= i
    # print(num)
    den = 1
    for i in range(1, n2 + 1):
        den *= i
    # print(den)
    coeff.append(num // den)#append use to take values in list

    r += 1
if n%2==0:
    f=coeff[r:0:-1]#slicing a[first:last:step] where first include and last exclude and blank take all input
else:
    f=coeff[r::-1]
f.extend(coeff)#extend use to take two list in one single list
print(f)