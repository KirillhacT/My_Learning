def hello(name):
    print("Hello", name, sep=", ")

#Присваивание функции
f = hello
f("Egor")

#Структурное программирование - задаем структуру проета с 
# помощью функций, которым даем подходящее название. Функции
# могут оставаться без реализации, ее оставляем на потом.
# Итогом проектирования станет структура, сделанная из функций
# с правильным именем, нуждающихся в реализации

def is_simple_number(x):
    """Проверяет, является ли число простым"""
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True
print(is_simple_number(16))

def factorize(x):
    """Раскладывает число на простые множители"""
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor, end=" ")
            x //= divisor
        else:
            divisor += 1
factorize(56734562)

 