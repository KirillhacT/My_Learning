#Сливание массивов
#TO DO!!!! merge, merge_sort, hoar_sort
# def merge(A: list, B: list):
#     C = [0] * (len(A) + len(B))
#     i = k = n = 0
#     while i < len(A) and k < len(B):
#         if A[i] <= B[i]:
#             C[n] = A[i]
#             i += 1
#             n += 1
#         else:
#             C[n] = B[k]
#             k += 1
#             n += 1
#     while i < len(A):
#         C[n] = A[i]
#         i += 1
#         n += 1
#     while k < len(B):
#         C[n] = B[k]
#         k += 1
#         n += 1
#     return C

# def merge_sort(A):
#     if len(A) < 2:
#         return
#     middle = len(A)//2
#     L = [A[i] for i in range(middle)]
#     R = [A[i] for i in range(middle, len(A))]
#     merge_sort(L)
#     merge_sort(R)
#     C = merge(L, R)
#     for x in range(len(A)):
#         A[x] = C[x]
#     print(A)
# merge_sort([5, 2, 4, 1, 2])

# def hoar_sort(A):
#     if len(A) < 2:
#         return None
#     barrier = A[0]
#     # L = M = R = []
#     L = []; M = []; R = []
#     for x in A:
#         if x < barrier:
#             L.append(x)
#         elif x == barrier:
#             M.append(x)
#         else:
#             R.append(x)
#     hoar_sort(L)
#     hoar_sort(R)
#     k = 0
#     for x in L+M+R:
#         A[k] = x
#         k += 1


def check_sorted(A, assending=True):
    """Проверка отсортированности за O(l(A)"""
    flag = True
    s = 2 * assending - 1
    for i in range(len(A)-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag

#Бинарный поиск

#Поиск левой границы
def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left
def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right
A = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6]
key = 5
a1 = left_bound(A, key)
a2 = right_bound(A, key)
print(a1, a2)



















































