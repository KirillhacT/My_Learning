#Решите задачу о количестве способов достичь точки n из точки 1, если кузнечик умеет прыгать +1, +2 и +3.
# N = int(input())
# F = [0, 1, 1] + [0] * (N - 2)
# for i in range(3, N+1):
#     F[i] = F[i - 1] + F[i - 2] + F[i - 3]
# print(F)

#Напишите функцию calculate_min_cost(n, price) вычисления наименьшей стоимость достижения клетки n из клетки 1
price = [1, 2, 1, 4, 1, 2, 4, 6, 7, 8, 1, 2]
N = len(price)
C = [0, 1] +  [0] * (N - 2)
for i in range(2, N):
    C[i] = min(C[i-1], C[i-2]) + price[i]
print(C)



