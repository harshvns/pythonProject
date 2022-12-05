a=[5,4,6,7,3,8]
mx1,mx2=a[0],a[1]
if mx2>mx1:
    mx1,mx2=mx2,mx1
n=len(a)
for i in range(2,n):
    value=a[i]
    if value<=mx2:
        continue
    if value>=mx1:
        mx2=mx1
        mx1=value
        continue
print("largest is:",mx1,"second largest is:",mx2)
