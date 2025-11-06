from math import *
i = ceil(log2(65536))
V = 3840 * 2160 * i
Vk = 16 * 2 ** 33
for n in range(20000, 722, -1):
    if n * V <= Vk:
        break
print(n * 14 + 722)



#2
i = ceil(log2(256))
V = 1280 * 1024 * i
Vk = 4 * 2 ** 33
for n in range(10**6, 307, -1):
    if V * n <= Vk:
        break
print(34 * n + 307)


#3
i = ceil(log2(256))
V = 1280 * 1024 * i
Vk = 4 * 2 ** 33
n = 8921742524
for i in range(10**6, 1, -1):
    if i * V <= Vk:
        break
print(n % i)


#4
i = ceil(log2(4096))
V = 1536 * 1024 * i
k = 150
U = 288 * 2 ** 13
t = 4 * 60
for j in range(1, 100):
    if V * k * j / 100 == U * t:
        break
print(1 - ceil(j))

#5
k1 = 2
j1 = 100 - 40
k2 = 1
j2 = 100 - 60
V1 = k1 * t * u * 
