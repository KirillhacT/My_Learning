#Динамическое программирование

#Нахождение n числа фибоначчи на динамическом программировании
n = 500
fib = [0, 1] + [0] * (n-1)
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]
# print(fib)

# def trage_num(n):
#     K = [0, 1] + [0] * n
#     for i in range(2, n+1):
#         K[i] = K[i-2] + K[i-1]
#     return K[n]

#Кол-во путей до клетки N, учитывая запрещенные значение, с шагом +1 +2 +3
def count_trage(N, allowed: list):
    K = [0, 1, int(allowed[2])] + [0] * (N-3)
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]
    return K[N]

#C[i] - cost - мин стоимость достижения клетки i

 #Минимальная стоимость достижения в клетку N
def count_min_cost(N, price: list):
    C = [float("-inf"), price[1], price[1]+price[2]] + [0]*(N-2)
    for i in range(3, N+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[N]

#Двумерный массив
M = 2
N = 3
# A = [[0] * M] * N #Неправильное создавание двумерного массива

A = [[0] * M for i in range(N)]
print(A)
print(A[0] is not A[1]) #is смотрит ссылается ли один объект на другой


































