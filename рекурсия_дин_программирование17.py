def fact2(n):
    f = [1] + [None] * n
    print(f)
    for i in range(1, n+1):
        f[i] = f[i-1] * i
    print(f)

#fibonacci на динамическом программировании
def fib2(n):
    f = [0] + [None] * n
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    print(f)

# fact2(10)
# fib2(5)

#fibonacci на рекурсии с хешированием
cash = {}
def fib(n: int) -> int:
    assert n >= 0 and n < 995
    if n not in cash:
        cash[n] = n if n < 2 else fib(n-1) + fib(n-2)
    return cash[n]
# print(fib(5))

N = 100
M = 12
m = []
v = []
#m - массы
#v - стоимости
F = [[0] * (N + 1) for i in range(M+1)]
for i in range(1, N+1):
    for k in range(1, M+1):
        if m[i] <= k:
            F[i][k] = max(F[i][k-1], v[i] + F[k-m[i][i-1]])
        else:
            F[i][k] = F[i][k-1]

