matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
#2d -> 1d
f = [i for lst in matrix for i in lst]
print(f)
f = []
for lst in matrix:
    for i in lst:
        f.append(i)
print(f)


#2d -> new 2d
new_matrix = [[i for i in lst] for lst in matrix]
print(new_matrix)
new_matrix = []
for lst in matrix:
    new_matrix.append(lst)
print(new_matrix)

#Условный оператор позволяют выполнять код в заивимости от выполнения определенных условий. if, elif, else (match-case с 3.10).
#Условия опираются на логические выражения, которые возвращают True (логическое единицей) или False (логический ноль)

#a = int(input('Введите число с клавиатуры: '))
'''
if a > 0:
    print('Положительное')
else:
    print('Отрицательное')
'''

'''
if a > 0:
    print('Положительное')
elif a == 0:
    print('Число равно нулю')
else:
    print('Отрицательное')
'''
'''
1) Чистый if
if a > 0:

2) if-else:
if a > 0:
    ....
else:
    ....

3) if-elif-else:
if a > 0:
    ....
elif a == 0:
    ....
else:
    ...

4) if-elif...

if a > 0:
    ....
elif a > 0
    ...
'''

#Короткая форма условия (тернарный оператор)
'''
a = int(input('Введите число с клавиатуры: '))

#Узнать, число больше 10 или меньше 10
if a > 10:
    print(f'Число {a} больше 10')
else:
    print(f'Число {a} меньше 10')

result = f'Число {a} больше 10' if a > 10 else f'Число {a} меньше 10' #в тернарном операторе нет eilf
print(result)

print(f'Число {a} больше 10' if a > 10 else f'Число {a} меньше 10')

print(f'Число {b} больше 10' if (b := int(input('Введите число с клавиатуры: '))) > 10 else f'Число {b} меньше 10') #:= - моржовый оператор, колторый позволяет присвоить значение внутри условия. реализовывать в скобках
'''
x, y = 5, 10
if x > 0:
    if y > 0:
        print('Оба положительные')
    else:
        print('x - положительное, y - нет')
else:
    if y > 0:
        print('x - отрицательное, y - положительное')
    else:
        print('Оба отрицательные')

#Логические операции

#and, or, not

'''
результат применения логической операции - True/False

and - логическое умножение, логическое И, конъюнкция, /\
a and b = F, and - оператор, a/b - операнды
0 and 0 = 0 
1 and 0 = 0
0 and 1 = 0
1 and 1 = 1

and возвращает True, если оба условия True

or - логическое сложение, логическое ИЛИ, дизъюнкиця, \/
a or b = F
0 or 0 = 0
1 or 0 = 1
0 or 1 = 1
1 or 1 = 1

or возвращает True, если хотя бы одно условие True
x = 5
x < 0 or x % 2 == 1
False or True = True

not - логическое отрицание, логическое НЕ, инверсия, ¬, ˜

not a = F
not 0 = 1
not 1 = 0
'''

#Короткое замыкание

'''
if a and b and c and d ....

В Python, если между всеми операндами стоит and, то будет остановка на первом False

if a or b or c or d ...

В Python, если между всеми операндами стоит or, то будет остановка на первом True
'''
#Интересные условия

#Проверить, есть ли элемент в объекте (список, строка ...)

#in - оператор проверки вхождения
lst = [1, 2, 3]
if 2 in lst:
    print('Элемент найден')

#Проверка на None или пустоту

#0, 0.0, None, [],(), {}, set() - False
lst = []
if not lst:
    print('Список пустой')

a = 0
if not a:
    print('Число равно нулю')

#Сравнение с несколькими значениями

#Проверить, равняется ли число 1, 2 или 3.

if x == 1 or x == 2 or x == 3:
    print('x - одно из значений')

if x in (1, 2, 3):
    print('x - одно из значений')

#match - case

'''
match - case - конструкция дл структурного соотвествия шаблону.
'''

status = 404
match status:
    case 200:
        print('ОК')
    case 404:
        print('Not Found')
    case _:
        print('Unknown') #case _ -неучтенные случаи. его писать необязательно

point = [1, 2]
match point:
    case [0, 0]:
        print('Начало координат')
    case [x, 0]:
        print(f"На оси X: {x}")
    case [0, y]:
        print(f"На оси Y: {y}")
    case _:
        print("Где-то еще")

lst = [1, 2, 3, 4]
match lst:
    case [x, y, w, z] if sum(lst) > 10: #может работать с if
        print('Сумма больше 10')
    case [x, y, w, z]:
        print('Сумма элементов равна 10 или меньше')

mark = 5 #0, 1, 2 - 2; 3, 4, 5 - 3; 6, 7, 8 - 4; 9, 10 - 5
match mark:
    case 0 | 1 | 2: #| - для комбинирования условий
        print(2)
    case 3 | 4 | 5:
        print(3)
    case 6 | 7 | 8:
        print(4)
    case 9 | 10:
        print(5)

#all(), any()

'''
all() - применяется к итерируемому объекту и возвращает True, если все элемента объекта True (and)
any() - применяется к итерируемому объекту и возвращает True, если хотя бы один элемент объекта True (or)
'''

x = [1, 2, 3, 4, 5, 6, 7]
#нужно проверить, все ли элементы внутри списка меньше 7
if all([i < 7 for i in x]): #[i < 7 for i in x] - [True, True, True, True, True, True, False]. Необязательно передавать список, так как работает с итераторами также
    print('Все элементы меньше 7')
else:
    print('Не все элементы меньше 7')

#нужно проверить, есть ли элементы внутри списка больше 6
if any([i > 6 for i in x]): #[i > 6 for i in x] - [False, False, False, False, False, False, True]. Необязательно передавать список, так как работает с итераторами также
    print('Хотя бы один элемент больше 6')
else:
    print('Нет элементов, больших 6')

matrix = [
    [1, 2],
    [3, 4]
]

#все элементы внутри матрицы больше нуля
if all([i > 0 for lst in matrix for i in lst]):
    print('Все элементы матрицы больше 0')
else:
    print('Есть элементы в матрице, которые меньше 0')


'''
Приоритет логических операций. Он меньше, чем у математических операторов и операторов сравнения.
not -> and -> or
'''

'''
Проверка списка на чётность
Вход: lst = [2, 4, 6]
Задача:

Проверьте, все ли элементы чётные с помощью all().
Если да, добавьте 0 в конец с append().
Выведите в f-строке: f"Список: {lst}, все чётные: {all_even}".
'''
lst = [2, 4, 6]
if all(i % 2 == 0 for i in lst):
    lst.append(0)
    print(f"Список: {lst}, все чётные: {lst}")

'''
Проверка строки на подстроку
Вход: s = "Hello, Python!"
Задача:

Проверьте, содержит ли строка "Python" с помощью in.
Если да, замените "Python" на "Code" с replace().
Выведите в f-строке: f"Строка: {s}, содержит Python: {has_python}".
'''

s = "Hello, Python!"
has_python = False
if "Python" in s:
    s = s.replace("Python", "Code")
    has_python = True
print(f"Строка: {s}, содержит Python: {has_python}")

'''
Проверка пустого списка
Вход: lst = []
Задача:

Проверьте, пустой ли список, используя if not lst.
Если пустой, добавьте "empty" с append().
Выведите в f-строке: f"Список: {lst}, пустой: {is_empty}".
'''
lst = []
is_empty = False
if not lst:
    lst.append("empty")
    is_empty = True
print(f"Список: {lst}, пустой: {is_empty}")
'''
Проверка строки на длину
Вход: s = "Python"
Задача:

Проверьте, больше ли длина строки 5 с помощью len().
Если нет, добавьте "!" с помощью конкатенации.
Выведите в f-строке: f"Строка: {s}, длина > 5: {is_long}".
'''
s = "Python"
is_long = True
if len(s) <= 5:
    s += "!"
    is_long = False
print(f"Строка: {s}, длина > 5: {is_long}")

'''
Проверка суммы строки матрицы
Вход: matrix = [[1, 2], [3, 4], [0, 0]]
Задача:

Проверьте, есть ли строка с суммой > 5 с помощью any().
Если нет, добавьте [6, 7] с append().
Выведите в f-строке: f"Матрица: {matrix}, есть сумма > 5: {has_sum}".
'''
matrix = [[1, 2], [3, 4], [0, 0]]
has_sum = True
if not any(sum(row) > 5 for row in matrix):
    matrix.append([6, 7])
    has_sum = False
print(f"Матрица: {matrix}, есть сумма > 5: {has_sum}")

'''
Проверка прямоугольности матрицы
Вход: matrix = [[1, 2], [3, 4], [5, 6]]
Задача:

Проверьте, одинакова ли длина всех строк с помощью all().
Если да, добавьте [7, 8] с append().
Выведите в f-строке: f"Матрица: {matrix}, прямоугольная: {is_rectangular}".
'''

matrix = [[1, 2], [3, 4], [5, 6]]
is_rectangular = False
if all(len(i) == 2 for i in matrix):
    matrix.append([7,8])
    is_rectangular = True
print(f"Матрица: {matrix}, прямоугольная: {is_rectangular}")

'''
Проверка строки на заглавные буквы
Вход: s = "HELLO"
Задача:

Проверьте, состоит ли строка из заглавных букв с isupper().
Если да, добавьте "!" с конкатенацией.
Выведите в f-строке: f"Строка: {s}, заглавные: {is_upper}".
'''
s = "HELLO"
is_upper = False
if s.isupper():
    s += "!"
    is_upper = True
print(f"Строка: {s}, заглавные: {is_upper}")
'''
Проверка списка на дубликаты
Вход: lst = [1, 2, 2, 3]
Задача:

Проверьте, есть ли дубликаты с помощью len(lst) != len(set(lst)).
Если да, удалите первое вхождение 2 с remove().
Выведите в f-строке: f"Список: {lst}, есть дубликаты: {has_duplicates}".
Обработайте ValueError.
'''
lst = [1, 2, 2, 3]
has_duplicates = False
if not len(lst) != len(set(lst)):
    has_duplicates = True
    try:
        lst.remove(2)
    except ValueError:
        print("errorrr")
print(f"Список: {lst}, есть дубликаты: {has_duplicates}")

