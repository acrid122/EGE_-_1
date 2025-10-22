print("Аделя")
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not(y <= (x == z)) and (w <= x):
                    print(x, y, w, z)

print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not((z <= y) or ((w <= x) <= y)):
                    print(x, y, w, z)
print("Аделя")
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not((x and not y) or (y == z) or w):
                    print(x, y, w, z)


print("Аделя")
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not(not(x <= y) or (z == w) or z):
                    print(x, y, w, z)

print("Аделя")
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if y and (z == (w <= (x or z))):
                    print(x, y, w, z)


print("Аделя")
print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a or b) <= (not c and a)) and d:
                    print(a, b, c, d)


print("Аделя")
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not((z <= (not(y <= x))) or w):
                    print(x, y, w, z)