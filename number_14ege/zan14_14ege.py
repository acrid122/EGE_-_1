for x in range(1, 3001):
    v = 9 ** 150 + 9 ** 30 - x
    count = 0
    while v > 0:
        if v % 9 == 0:
            count += 1
        v //= 9
    if count == 122:
        print(x)
        break


def f(number, base):
    s = ''
    while number > 0:
        s += str(number % base)
        number //= base
    return s[::-1]

print(f(182, 4))
print(182 % 4)
print(int('100002', 4))

count = 0
for x in range(1026, 4097):
    if x % 4 == 2 and (x // 16) % 16 == 14: #целочисленное деление
        count += 1
print(count)

import string
import math 

s = string.digits + string.ascii_uppercase

sp = []
for x in s[:15]:
    M = int(f'432{x}3', 15)
    N = int(f'86{x}86', 15)
    res = math.ceil(M / N)
    new_M = res * N
    A = new_M - M
    sp.append(A)
print(min(sp))

def f2(number, base):
    s = ''
    s1 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s1[number % base]
        number //= base
    return s[::-1]

for n in range(5, 37):
    ch1 = f2(41, n)
    ch2 = f2(131, n)
    if ch1[-1] == '2' and ch2[-1] == '1':
        print(n)
        
