sp = []
for n in range(1, 10**4):
    bin_n = bin(n)[2:]
    if n % 3 == 0:
        bin_n += bin_n[-3:]
    else:
        bin_n += bin((n % 3) * 3)[2:]
    r = int(bin_n, 2)
    if r < 130:
        sp.append(n)
print(max(sp))

def f(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n = n // 7
    return s[::-1]

sp = []
for n in range(1, 10**4):
    seven_n = f(n)
    summa = sum(int(i) for i in str(seven_n))
    if summa % 2 == 0:
        seven_n += '555'
    else:
        seven_n = '33' + seven_n + '6'
    r = int(seven_n, 7)
    if r < 12717:
        sp.append(n)
print(max(sp))


import string
def f1(n):
    s = ''
    s1 = string.digits + string.ascii_uppercase
    while n > 0:
        s += s1[n % 3]
        n = n // 3
    return s[::-1]



sp = []
for n in range(1, 10**4):
    tn = f1(n)
    summa = sum(map(int, tn))
    if summa % 3 == 0:
        table = str.maketrans('01', '10')
        tn = tn.translate(table)
        tn = '10' + tn
    else:
        tn += '101'
        tn = '22' + tn[2:]
    r = int(tn, 3)
    if r > 314:
        sp.append((n, r))
sp.sort(key = lambda x: (x[1], x[0]))
print(sp[:10])