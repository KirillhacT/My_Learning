A = [True, 2, 5.3, "Hello"]

#B - кортеж
B = (True, 2, 5.3, A)

"""
>>> x = 2
>>> y = 2
>>> x is y
True
"""
print(B)
A[0] = False
print(B)


C = [(1, 5), (-3, 4), (-7, 2), (8, 3), (0, 0)]
# for pt in C:
#     print(pt[0], pt[1])

#Лучше писать
# for x, y in C:
#     print(x, y)

x = 2
y = 3
E = x, y

#Распаковка
a, b = E
print(a, b)
