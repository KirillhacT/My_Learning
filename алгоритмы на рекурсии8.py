#Генерация всех перестановок

def gen_bin(M, mas, prefix=''):
    if M == 0:
        print(prefix)
        return
    # gen_bin(M - 1, prefix+"0")
    # gen_bin(M - 1, prefix + "1")
    for digit in mas:
        gen_bin(M-1, mas, prefix+digit)



def generate_numbers(N: int, M: int, prefix=None):
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

# gen_bin(3, [str(i) for i in range(1, 4 )])

def generate_permutation(N: int, M: int=-1, prefix=None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutation(N, M-1, prefix)
        prefix.pop()


def find(number, A):
    """Ищет число в массиве и возвращает true, если оно там есть"""
    for i in A:
        if number == i:
            return True
    return False
# generate_permutation(2)

    



