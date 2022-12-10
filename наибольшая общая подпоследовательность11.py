from pprint import pprint

def print_massive(F):
    for i in F:
        for j in i:
            print(j, end=" ")
        print()

#Нахождение длины наибольшей подпоследовательности
def lcs(A, B):
    F = [[0] * (len(B)+1) for i in range(len(A) + 1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
            print_massive(F)
            print()

    return F[-1][-1]

print(lcs([1, 2], [1, 2]))

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in a:
#     for j in i:
#         print(j, end=" ")
#     print()

#Наибольшая возрастающая подпоследовательность
# def gis(A):
#     F = [0] * (len(A) + 1)
#     for i in range(1, len(A)):
#         m = 0
#         for j in range(0, i):
#             if A[i] > A[j] and F[j] > m:
#                 m = F[j]
#         F[i] = m + 1
#     return F[len(A)]
# print(gis([1, 2, 3, 4, 5]))






