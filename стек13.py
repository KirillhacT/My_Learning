# _stack = []
# def push(x):
#     """
#     Добление элемента x в конец стека
#     >>> size = len(_stack)
#     >>> push(5)
#     >>> len(_stack) - size
#     1
#     >>> _stack[-1]
#     5
#     """
#     _stack.append(x)
# def pop():
#     x = _stack.pop()
#     return x
# def clear():
#     _stack.clear()
# def is_empty():
#     return len(_stack) == 0

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        x = self._stack.pop()
        return x

    def clear(self):
        self._stack.clear()

    def is_empty(self):
        return len(self._stack) == 0

# stack1 = Stack()
# print(stack1.is_empty())
# stack1.push(1)
# stack1.push(2)
# stack1.push(3)
# print(stack1.is_empty())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.is_empty())


#Проверка корректности скобочной последовательности
"""
Корректные:
A = ""
B = (A)
B = [A]
B = {A}
C = AB  
"""
stack = Stack()
def is_braces_sequences_correct(s: str) -> bool:
    """Проверяет корректность скобочной последовательности
    >>> is_braces_sequences_correct("(([()]))[]")
    True
    >>> is_braces_sequences_correct("([)]")
    False
    >>> is_braces_sequences_correct("([]")
    False
    >>> is_braces_sequences_correct("(")
    False
    >>> is_braces_sequences_correct("]")
    False
    """
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            stack.push(brace)
        else:
            assert brace in ")]", f"Ожидалась закрывающаяся скобка: {str(brace)}"
            if stack.is_empty():
                return False
            left = stack.pop()
            assert left in "([", f"Ожидалась открывающая скобка: {str(brace)}"
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Обратная польская нотация
# Алгоритм вычисления выражения в постфиксной нотации

# [5, 2, "+"] <=> 5 + 2
# (2 + 7) * 5 <=> [2, 7, "+", 5, "*"]
# 2 + 7 * 5 <=> [2, 7, 5, "*", "+"]
stack2 = Stack()
a = [5, 2, "+"]
b = [2, 7, "+", 5, "*"]
c = [2, 7, 5, "*", "+"]
def polskay_notation(a):
    for token in a:
        if isinstance(token, int):
            stack2.push(token)
        else:
            y = stack2.pop()
            x = stack2.pop()
            z = 0
            if token == "+":
                z = x + y
            elif token == "*":
                z = x * y
            stack2.push(z)
    result = stack2.pop()
    return result
print(polskay_notation(a))
print(polskay_notation(b))
print(polskay_notation(c))

