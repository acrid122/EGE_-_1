for t in range(1000, 0, -1):
    V_frame = 1920 * 1080 * 16
    V_frame_second = V_frame * 20
    V_audio = 2 * 44000 * 16 * t
    if (V_audio + V_frame_second * t) <= 3123 * 2 ** 23:
        print(t)
        break

from math import log2, ceil

N = 65536
i = ceil(log2(N)) #log2 - логарифм по основанию два, ceil - округление в большую сторону
#int(), //, floor из math - округление в меньшую сторону
#512 % n = 52
#n = 5 -> %= 2, / = 102, 4
#n количество фотографий на одной карточке
for n in range(1, 1000):
    if 512 % n == 52:
        break
V = 1920 * 1080 * i
print(ceil((n * V)/ 2 ** 23))

i = ceil(log2(65536))
j = i
for n in range(1000, 0, -1):
    V = 3840 * 2160 * (i + j)
    if V * n <= 8 * 2 ** 33:
        break
total = n * 2 + 45
print(ceil(total / 10))