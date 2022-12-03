#поиск элемента в массивк
def array_search(A: list, x: int):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return None
print(array_search([i**2 for i in range(10)], 64), end="\n\n")

#reverse массива
def invert_array(A: list):
    N = len(A)
    for i in range(N//2):
        A[i], A[N-1-i] = A[N-1-i], A[i]
    return A
print(invert_array([1, 2, 3, 4, 5]))
#Второй вариант
a1 = lambda A: A[::-1]
print(a1([1, 2, 3, 4, 5]), end="\n\n")

#циклический сдвиг влево
def sdvig_vlevo(A):
    N = len(A)
    tmp = A[0]
    for i in range(N-1):
        A[i] = A[i+1]
    A[N-1] = tmp
    return A
print(sdvig_vlevo([1, 2, 3, 4, 5]), end="\n\n")
#2 3 4 5 1

#циклический сдвиг вправо
def sdvig_vpravo(A):
    N = len(A)
    tmp = A[N-1]
    for i in range(N-2, -1, -1):
        A[i+1] = A[i]
    A[0] = tmp
    return A
#5 1 2 3 4

print(sdvig_vpravo([1, 2, 3, 4, 5]), end="\n\n")

def resheto_eratosphena(N: int):
    A = [True] * N
    A[0] = A[1] = False
    for i in range(2, N):
        if A[i]:
            for m in range(i+i, N, i):
                A[m] = False
    return A

print(resheto_eratosphena(10))
        




