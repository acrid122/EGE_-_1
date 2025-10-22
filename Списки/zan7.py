'''
Вложенные списки - это списики, содержащие другие списки в качестве элементов.
[[1, 2], [3, 4], [5, 6]] - двумерный список (матрица)

_ 1 2
1 1 2
2 3 4
3 5 6
'''

a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10]]]
print(a[0][0][0])

'''
copy() - поверхностная копия.
deepcopy() - глубокая копия.
'''

b = [[1, 2], [3, 4], [5, 6]]
c = b.copy()
c[0][0] = 9
print(b)

import copy

d = copy.deepcopy(b)
d[0][0] = 1
print(b)

'''
[[x, o, x], [3, 4], [5, 6]]
'''
#Матрица 3x3 с нулями

matrix = [[0] * 3 for i in range(3)]
print(matrix)
matrix[0][0] = 2
print(matrix)
matrix = [[0 for i in range(3)] for j in range(3)]
print(matrix)
matrix = [[0] * 3] * 3 #все подсписки ссылаются на один и тот же объект. этот способ самый плохой
print(matrix)
matrix[0][0] = 2
print(matrix)
'''
[[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix = [[i * 2 for i in row] for row in matrix]
print(matrix)

tr = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
tr = [[[i * 2 for i in row2] for row2 in row] for row in tr]
print(tr)

#развернуть список 2d в список 1d

#[[1, 2], [3, 4]] - [1, 2, 3, 4]
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

#matrix = [i for row in matrix for i in row]

sp = []
for row in matrix:
    for i in row:
        sp.append(i)
print(sp)

print(matrix)

#map - map(func, iterable). возвращает итератор

result = list(map(int, sp))

#преобразовать список строк в верхний регистр

words = ['cat dsad', 'dog dasddasdasdaa']
upper = list(map(str.upper, words))
print(upper)

l = [
    [1, 2], 
    [3, 4], 
    [5, 6]
]
summ = list(map(sum, l))
print(summ)

p = list(map(str.capitalize, words))
print(p)

words.sort(key = len, reverse = True)
print(words)

numbers = [[1, 2], [3, 4], [0, 2], [0, -1]]
numbers.sort(key = sum)
print(numbers)

numbers.sort() #работает по возрастанию и по умолчанию сравнивает элементы вложенных структур по индексам
print(numbers)

numbers.sort(key = lambda x: (x[1], -x[0]))
print(numbers)

#numbers = [1, 2, 3] -> numbers = [1, 4, 9]

numbers = [1, 2, 3]
numbers = list(map(lambda x: x ** 2, numbers))
print(numbers)

numbers = [1, 2, 3]
#numbers = [1, 2, 3] -> numbers = [-1, 0, 1]
numbers = list(map(lambda x: x - 2, numbers))
print(numbers)

#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8] -> numbers = [0, 1, 0, 1, 0, 1, 0, 1, 0]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers = list(map(lambda x: x % 2, numbers))
print(numbers)