count=0
a = [12,3,4,5,7,6]
n = len(a)
for i in range(0, n - 1):
    # swapped=False
    for j in range(0, n - i - 1):
        # count+=1
        if a[j] > a[j + 1]:
            # swapped=True
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t
    # if not swapped:
    #     break

print(a)
# print(count)