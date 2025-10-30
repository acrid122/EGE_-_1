for x in range(3000, 0, -1):
    ch = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    count = 0
    while ch > 0:
        if ch % 11 == 0:
            count += 1
        ch //= 11
    if count == 60:
        print(x)
        break
        
for x in range(2400, 0, -1):
    z = 7 * 9 ** 210 + 6 * 9 ** 110 - x
    count = 0
    while z > 0:
        if z % 9 == 0:
            count += 1
        z //= 9
    if count == 100:
        print(x)
        break

p = int('1300220', 4)
print(p)
for x in range(7208, 8172):
    if (x // 4) % 4 == 2 and (x // 16) % 4 == 2 and (x // 4 ** 5) % 4 == 3 and (x // 4 ** 6) % 4 == 1:
        if x % 8 == 0 and (x // 8) % 8 == 5 and (x // 8 ** 4) % 8 == 1 \
        and x % 16 == 8 and (x // 16) % 16 == 2 and (x // 16 ** 2) % 16 == 12:
            print(x)

import string
s = string.digits + string.ascii_uppercase
s1 = set() #сооздаю пустое множество, которое хранит (как и любое множество) только уникальные элементы
for x in s[1:25]:
    ch1 = int(f'8AF7{x}11', 25)
    ch2 = int(f'{x}DA87', 25)
    r = ch1 + ch2
    for y in range(1, 101):
        if r % y == 0:
            s1.add(y) #метод .add() для добавления
print(len(s1))