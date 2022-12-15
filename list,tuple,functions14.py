# О кортежах
# A = [True, 2, 5.3, "Hello"]
#
# #B - кортеж
# B = (True, 2, 5.3, A)
#
# """
# >>> x = 2
# >>> y = 2
# >>> x is y
# True
# """
# print(B)
# A[0] = False
# print(B)
#
#
# C = [(1, 5), (-3, 4), (-7, 2), (8, 3), (0, 0)]
# # for pt in C:
# #     print(pt[0], pt[1])
#
# #Лучше писать
# # for x, y in C:
# #     print(x, y)
#
# x = 2
# y = 3
# E = x, y
#
# #Распаковка
# a, b = E
# print(a, b)

#О срезах
s = "hello"
s1 = s[:] # s[:] - все элементы
s2 = s[::-1] # С начала до конца
print(s1)
print(s2)
A = [0, 1, 2, 3, 4]
B = A[:]
A[0] = 12
print(B[0])

b = "abcdefgh"
x = b
b = b[::2] + b[::-2]
print(b)


A = [0, 1, 2, 3, 4]
A[0:3] = [10, 20, 30, 40]
print(A)
A[0:3] = []
print(A)

#Куча - Heap


