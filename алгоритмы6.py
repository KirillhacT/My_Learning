#Тернарный оператор if
a = 4
b = a ** 2 if a % 2 == 0 else a
# print(b)

#Квадратичные сортировки (вставками, выбором, пузырьком)
def insert_sort(A):
    """Сортировка вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        #так как and в python является ленивым, то выхода за границы массива не будет
        while (k > 0) and (A[k-1] > A[k]):
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choices_sort(A):
    """Сортировка выбором"""
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    N = len(A)
    """Сортировка пузырьком"""
    for i in range(N-1):
        for j in range(N-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


def test(sort_algoritm):
    print(f"Тестируем: {sort_algoritm.__doc__}")
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algoritm(A)
    print("OK" if A == A_sorted else "FAIL")




if __name__ == "__main__":
    pass
    # test(insert_sort)
    # test(choices_sort)
    # test(bubble_sort)