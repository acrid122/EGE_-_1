'''
Цикл for используется для перебора элементов итерируемого объекта (список, строка, кортеж, диапазон и т.д.).

for variable in iterable:
    #Код
'''
lst = [1, 2, 3]
for elem in lst:
    print(elem, end = ' ') #end - параметр print(), который задает символ после вывода очередного элемента

print()

for elem in lst:
    elem = 1 #elem - копия элемента списка. в данном случае просто меняется копия
print(lst)

for i in range(len(lst)): #range(len(lst)) = range(3) = 0, 1, 2
    lst[i] = 1
print(lst)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for lst in matrix:
    for elem in lst:
        elem = 1
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = 1
print(matrix)

#Нюансы

'''
Не надо изменять итерируемый объект внутри цикла (remove/append/pop/replace (если на пустую) и т.д.)
lst = [1, 2, 3]
for elem in lst:
    lst.append(4)
'''

'''
Цикл while. Цикл по условию. Выполняется, пока условие истинно.

while condition:
    ...
'''

'''
Нюансы.

1) Угроза бесконечного цикл.
2) Нет захода в цикл
'''

#1 нюанс

x = 0
while x < 5:
    print(x)
    x += 1 #инкремент, увеличение на 1

#2 нюанс

x = 0
while x > 5:
    print(x)

#Бесконечный цикл

#while True:, while 1:

#break/continue

#break - оператора досрочного выхода из цикла (прерывания цикла)

for x in range(5):
    if x == 3:
        break
    print(x)

print()

for x in range(5):
    print(x)
    if x == 3:
        break

print()

for x in range(5):
    if x == 3:
        print(x)
        break

print()

for x in range(5):
    if x == 3:
        break
        print(x)

#continue - оператор, который пропускает текущую итерацию и переходит к следующей. При срабатывании пропускает все строчки кода, находящиеся под ним в рамках цикла
print()

for x in range(5):
    if x == 3:
        continue
    print(x)

print()

for x in range(5):
    print(x)
    if x == 3:
        continue

print()

for x in range(5):
    if x == 3:
        print(x)
        continue

print()

for x in range(5):
    if x == 3:
        continue
        print(x)

#break и continue в рамках while работают одинаково

'''
x = 0
while x < 5:
    if x == 3:
        continue #надо быть аккуратным, так как conitnue пропустит и инкремент
    print(x)
    x += 1
'''
x = 0
while x < 5:
    if x == 3:
        x += 1
        continue
    print(x)
    x += 1

#for-else, while-else

'''
Если внутри цикла срабатывает break, то блок кода, описанный в else не выполняется. Иначе выполняется
'''

lst = [i for i in range(1, 8)]
for elem in lst:
    if elem == 9:
        print('Найдено')
        break
else:
    print('Чисел не найдено')

i = 0
while i < len(lst):
    if lst[i] == 2:
        print('Найдено')
        break
    i += 1
else:
    print('Чисел не найдено')

names = ['Alice', 'Bob', 'Skyler', 'Walter']
scores = [95, 80, 70, 60]

for i in zip(names, scores):
    print(i)

for name, score in zip(names, scores):
    print(name, score)

matrix = [
    ['Alice', 90, 18],
    ['Bob', 80, 19],
    ['Anna', 90, 15]
]

for name, score, age in matrix:
    print(name, score, age)

#enumerate(iterable, start = 0) - возвращает итератор кортежей. (индекс, элемент)

lst = [90, 80, 70]
for index, elem in enumerate(lst):
    print(index, elem)

for index, elem in enumerate(lst, 1000):
    print(index, elem)

'''
Сумма чётных чисел
Вход: lst = [1, 2, 3, 4]
Задача:

Используйте for для подсчёта суммы чётных чисел.
Выведите: f"Список: {lst}, сумма чётных: {total}".
'''
lst = [1, 2, 3, 4]
summa = 0
for i in lst:
    if i % 2 == 0:
        summa += i
print(summa)

print(sum(i for i in lst if i % 2 == 0))
'''
Поиск первого отрицательного
Вход: lst = [1, 2, -3, 4]
Задача:

Используйте while для поиска первого отрицательного числа.
Если найдено, прервите цикл с break.
Выведите: f"Список: {lst}, первое отрицательное: {result}".
'''
lst = [1, 2, -3, 4]
i = 0
result = 0

while lst[i] >= 0:
    i += 1

result = lst[i]
print(f"Список: {lst}, первое отрицательное: {result}")

'''
Пропуск нечётных
Вход: lst = [1, 2, 3, 4]
Задача:

Используйте for с continue для вывода только чётных чисел.
'''
lst = [1, 2, 3, 4]
for i in lst:
    if i % 2 != 0:
        continue
    print(i)
'''
Проверка на нули
Вход: lst = [1, 0, 3]
Задача:

Используйте for с else для проверки наличия нулей.
Если нули есть, прервите цикл.
Выведите: f"Список: {lst}, нули есть: {has_zeros}".
'''
lst = [1, 0, 3]
for i in lst:
    if i == 0:
        print(f"Список: {lst}, нули есть: {True}")
        break
else:
    print(f"Список: {lst}, нули есть: {False}")

'''
Удвоение элементов матрицы
Вход: matrix = [[1, 2], [3, 4]]
Задача:

Используйте вложенный for для удвоения каждого элемента.
Выведите: f"Матрица: {matrix}".
'''
matrix = [[1, 2], [3, 4]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] *= 2
print(f"Матрица: {matrix}")
'''
Объединение списков
Вход: lst1 = [1, 2], lst2 = ["a", "b"]
Задача:

Используйте zip для создания пар (число, строка).
Выведите: f"Пары: {pairs}".
'''

lst1 = [1, 2]
lst2 = ["a", "b"]
pairs = list(zip(lst1, lst2))
print(f"Пары: {pairs}")

'''
Транспонирование матрицы
Вход: matrix = [[1, 2], [3, 4]]
Задача:

Используйте zip(*matrix) для транспонирования.
Выведите: f"Транспонированная: {transposed}".
'''
matrix = [
    [1, 2], 
    [3, 4]
]
transposed = zip(*matrix) #* - распаковка zip([1, 2], [3, 4])
print(f"Транспонированная: {list(transposed)}")

'''
Удвоение по индексу
Вход: lst = [1, 2, 3]
Задача:

Используйте enumerate для удвоения элементов с чётными индексами.
Выведите: f"Список: {lst}"
'''
lst = [1, 2, 3]
for i, j in enumerate(lst):
    if i % 2 == 0:
        j *= 2
print(f"Список: {lst}")

'''
Индексация списка
Вход: lst = ["a", "b", "c"]
Задача:

Используйте enumerate для вывода индексов и элементов.
Выведите: f"Пары: {pairs}".
'''
lst = ["a", "b", "c"]
for index, elem in enumerate(lst):
    print(f"Пары:{index, elem}")