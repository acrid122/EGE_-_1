from math import log2, ceil
i = ceil(log2(65536))
V = 3840 * 2160 * i
for n in range(10000, 1, -1):
    if V * n <= 16 * 2 ** 33:
        break
total = n * 14 + 722
print(total)

from math import log2, ceil
i = ceil(log2(256))
V = 1280 * 1024 * i
for n in range(10000, 1, -1):
    if V * n <= 4 * 2 ** 33:
        break
total = n * 34 + 307
print(total)

i = ceil(log2(256))
V = 1280 * 1024 * i
for n in range(10000, 0, -1):
    if V * n <= 4 * 2 ** 33:
        break
print(8921742524 % n)


i = ceil(log2(4096))
V = 1536 * 1024 * i
for k in range(100, 0, -1):
    if 150 * V * k / (100 * 288 * 2 ** 13) == 240:
        print(k)



