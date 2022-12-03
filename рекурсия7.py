def matryoshka(n):
    if n == 1:
        print("Матрешка")
    else:
        print("Вверх матрешки n=", n)
        matryoshka(n-1)
        print("Низ матрешки n=", n)

def factorial(n):
    if n == 1:
        return n
    return factorial(n-1) * n

fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)


# matryoshka(5)
# print(factorial(10))
# print(fib(10))

#Алгоритм Евклида
# def gcd(a, b):
#     if a == b:
#         return a
#     elif a > b:
#         return gcd(a - b, b)
#     return gcd(a, b - a)

def gcd2(a, b):
    """
    16, 4
    4, 16 % 4 -> 4, 0
    4 возвращает

    26, 3
    3, 26 % 3 -> 3, 2
    2, 3 % 2 -> 2, 1
    1, 2 % 1 -> 1, 0
    возвращает 0
    """
    if b == 0:
        return a
    return gcd2(b, a % b)

gcd3 = lambda a, b: a if b == 0 else gcd2(b, a % b)
print(gcd3(16, 4))

#Быстрое возведение в степень - (только для положительных целых чисел)
def pow(a: float, n: int) -> float:
    if n == 0:
        return 1
    return pow(a, n-1) * a
print(pow(2, 5))

def pow2(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1: #Нечетное
        return pow(a, n-1) * a
    return pow(a ** 2, n // 2) * a
