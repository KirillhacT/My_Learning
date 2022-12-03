#В десятичной системе 
x = 0b10
#В восьмиричной системе
y = 0o34
#В шестнадцатиричной системе
z = 0xF


t = int('Z3F', base=36)
#t - число в 36 ричной системе
print(t)

xin = 120
print(bin(xin))
print(oct(xin))
print(hex(xin))

base = 7
string = ""
N = int(input())
while N > 0:
    digit = N % base
    string += str(digit)
    N //= base
print(string[::-1])