sp = []
for n in range(1, 10 ** 4):
    bin_n = bin(2 * n)[2:]
    sum_n = sum(map(int, bin_n)) #сумма цифр двоичной записи. ch = 1000, sum(map(int, str(ch))).
    #еще один способ: bin_n.count('1')
    bin_n += str(sum_n % 2)
    sum_n = sum(map(int, bin_n))
    bin_n += str(sum_n % 2)
    r = int(bin_n, 2)
    if r > 249:
        sp.append(n)
print(min(sp))

import string

def f1(number):
    s = ''
    s1 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s1[number % 6]
        number //= 6
    return s[::-1]

sp = []
for n in range(1, 10 ** 4):
    sixth = f1(n)
    sum_n = sum(map(int, sixth))
    if sum_n % 5 == 0:
        #sixth = sixth.replace('0', '@').replace('3', '0').replace('@', '3')
        table = str.maketrans('03', '30')
        sixth = sixth.translate(table)
        sixth = '11' + sixth
    else:
        sixth += '44'
        sixth = sixth.replace(sixth[1], '0', 1).replace(sixth[2], '5', 1)
    r = int(sixth, 6)
    if r > 1500:
        sp.append((n, r))
sp.sort(key = lambda x: (x[1], -x[0]))
print(sp[:10])


sp = []
for n in range(10 ** 3, 10 ** 4):
    numbers = list(map(int, str(n))) #разбить число на цифры
    pr = [numbers[0] * numbers[i] for i in range(1, 4)]
    pr.sort()
    if ''.join(map(str, pr[1:])) == '5472':
        sp.append(n)
print(min(sp))

import math

sp = []
for n in range(10 ** 4, 10 ** 5):
    numbers = list(map(int, str(n))) #разбить число на цифры
    sum_kv = (max(numbers) + min(numbers)) ** 2
    pr = math.prod([i for i in numbers if i % 2 == 0]) #prod - перемножает все элементы итерируемого объекта
    if ''.join(map(str, sorted([sum_kv, pr], reverse = True))) == '12116':
        sp.append(n)
print(min(sp))

def f2(number):
    s = ''
    s1 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s1[number % 4]
        number //= 4
    return s[::-1]

sp = []
for n in range(1, 10 ** 4):
    fourth = f2(n)
    count_zn = len(fourth) #sum([1 for i in fourth if i in '123']) сумма значащих цифр, но без нуля
    if count_zn % 2 == 0:
       fourth = fourth[:count_zn // 2] + '0' + fourth[count_zn // 2:]
    r = int(fourth)
    if r <= 180:
        sp.append(n)
print(max(sp))

#можем делать без списка, так как результатом будет являться только 1 какое-то N
for n in range(1, 128):
    bin_n = bin(n)[2:].zfill(8) #строим восьмибитную запись
    table = str.maketrans('01', '10')
    bin_n = bin_n.translate(table)
    r = int(bin_n, 2) + 1
    r = int(bin(r)[2:], 2)
    if r == 153:
        print(n)
        break