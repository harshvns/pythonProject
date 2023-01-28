a = [3, 7, 5, 2, -9]
n = len(a)
print(a)
for i in range(0, n - 1):
    minpos = i
    for j in range(i + 1, n):
        if (a[j] < a[minpos]):
            minpos = j
    t = a[i]
    a[i] = a[minpos]
    a[minpos] = t
    print(a)
print(a)
