sp = []
for p in range(7,37):
    ch1 = int("2465123", p)
    ch2 = int("251341", p)
    r = ch1 + ch2
    if r % 17 == 0:
        print(r // 17)
        break


s = 17 * 125 ** 453+ 117 * 5 ** 231 - 3 * 5 ** 13 - 2357
count = 0
while s > 0:
    if s % 125 <= 37:
        count += 1
    s //= 125
print(count)  


s = 2 * 2401 ** 525 + 3 * 343 ** 524 - 4 * 49 ** 523 + 5 * 49 ** 522 - 6 * 7 ** 521 - 35
count = 0
while s > 0:
    if s % 49 <= 9:
        count += 1
    s //= 49
print(count)

import string

s = string.digits + string.ascii_uppercase
for x in s[:29]:
    ch1 = int((f'463{x}7921'), 29)
    ch2 = int((f'8241{x}153'), 29)
    r = ch1 + ch2
    if r % 28 == 0:
        print(r // 28)
        break

import string
s = string.digits + string.ascii_uppercase
for x in s[:14]:
    ch1 = int((f'4B3{x}1'), 14)
    ch2 = int((f'5{x}F83'), 16)
    r = ch1 + ch2
    if r % 13 == 0:
        print(r // 13)
        break

for x in range(1, 13):
    ch1 = 13 ** 0 * int('B', 13) + 13 ** 1 * int('A', 13) + 13 ** 2 * x + 13 ** 3 * 9
    ch2 = 16 ** 0 * int('C',16) + 16 ** 1 * 6 + 16 ** 2 * 4 + 16 ** 3 * x
    ch3 = 15 ** 0 * x + 15 ** 1 * 7 + 15 ** 2 * int('B', 15)
    r = ch1 + ch2 - ch3
    if r % 14 == 0:
        print(r // 14)