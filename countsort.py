a = [8, 5, 0, 3, 1, 6, 9, 7]
n = len(a)
output = [0 for i in a]
f = [0 for i in range(10)]
for i in a:
    f[i] += 1
print(f)
for i in range(1, 10):
    f[i] += f[i - 1]
print(f)
for i in range(n - 1, -1, -1):
    value = a[i]
    pos = f[value]
    output[pos - 1] = value
    f[value] -= 1
print(output)
