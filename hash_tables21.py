# A = {1, 2, 3}
#
# A = set("rat")
# print("r" in A)
# A.add(5)
# print(A)

a = "aba"
b = {}
for i in range(len(a)):
    k = a[i]
    if k not in b:
        b[k] = 1
    else:
        b[k] += 1
print(b)