sp = []
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    bin_n += bin_n[-3:] if n % 3 == 0 else bin((n % 3)* 3)[2:]
    r = int(bin_n, 2)
    if r < 130:
        sp.append(n)
print(max(sp))

import string

def f(number):
    s = ''
    s2 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s2[number % 7]
        number //= 7 
    return s[::-1]


sp = []
for n in range(1, 10000):
    l = f(n)
    if sum(map(int, str(n))) % 2 == 0:
        l += '555'
    else:
        l = '33' + l + '6'
    r = int(l, 7)
    if r < 12717:
        sp.append(n)
print(max(sp))


      
    