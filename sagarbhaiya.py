s1 = "dog"
s2 = "god"
count = 0
for i in range(len(s1)):
    if s1[i] in s2:
        count += 1
if len(s1)!=len(s2):
    print("not anagram")

elif count == len(s1):
    print("anagram")
else:
    print("not anagram")
