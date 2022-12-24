# class Goat:
#     is_goat: bool = True
#     def __init__(self, height, weigth):
#         self.height = height
#         self.weight = weigth
#
#     def __str__(self):
#         s = f"""weight={self.weight}, height={self.height}"""
#         return s
#
# marusya = Goat(60, 40)
# notka = Goat(65, 42)
#
# for x in marusya, notka:
#     print(x)

#Связный список
import django.db.models

a = ["begin"]
a.append([1])
a[1].append([2, a])
print(a)

#Обход списка
# p = a
# count = 0
# while p is not None:
#     if count > 10:
#         break
#     print(p[0])
#     p = p[1]
#     count += 1

N = 10 ** 6
A = [0] * N
# a = A
# a.insert(0, 1) #Вставить в позицию 0 1

#Реализация связанного списка
class LinkedList:
    def __init__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        assert self._begin is not None, "List empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x


a = LinkedList()
a.insert(5)
a.insert(10)
print(a.pop())
print(a.pop())
# print(a.pop())







