a, b, c = 1, 3, 2
print(a, b, c)
maxnumber = (a if a >= c else c) if a >= b else (b if b >= c else c)
print(maxnumber)
