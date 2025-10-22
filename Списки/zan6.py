'''
Списки (list) - упорядоченные, изменяемые коллекции данных в Python.
Они могут содержать элементы любого типа (числа, строки, другие списки, объекты) и поддерживают динамическое изменение размера.
'''
import array

s = array.array('i', [1, 2, 3, 4])

#Создание списков
empty_list = [] #empty_list = list()
numbers = [1, 2, 3, 4]
mixed = [1, 'hello', 3.14, [5, 6], True]
repeats = [1] * 10
add_list = [1, 2, 3] + [4, 5]

print(empty_list, numbers, mixed, repeats, add_list)
'''
Особенности:

Упорядоченные: элементы сохраняют порядок добавления.
Изменяемые: можно менять элементы, добавлять или удалять.
Поддерживают дубликаты: [1, 1, 2] — допустимый список.
Динамические: размер меняется автоматически.
'''

'''
Индексация (точно такая же, как в строках)
'''

lst = ['apple', 'banana', 'cherry', 'lemon', 'melon']
print(lst[4], lst[-1])

'''
Срезы (точно такие же, как в строках)
'''
print(lst[1:4], lst[1:-1])
print(lst[::2])
print(lst[:3])

'''
Изменение
'''

lst[-1] = 'orange'
print(lst)

lst[-2:] = ['orange', 'pineapple']
print(lst)

a = [1, 2, 3]
b = a
b.append(4) #ссылается на один и тот же объект
print(a)

'''
Методы списков
'''

#1. .append(x). Добавляет элемент x в конец списка

c = [1, 2, 3]
c.append(4)
print(c)

c.append([5, 6]) #добавит в конец список [5, 6]
print(c)

#2. .extend(iterable). Добавляет все элементы из итерируемого объекта в конец списка

c.extend([7, 8])
print(c)

#3. .insert(i, x). Вставляет элемент x по индексу i

c.insert(1, 9)
print(c)

#4. .remove(x). Удаляет первое вхождение элемента x. Вызывает ValueError, если x нет

try:
    c.remove(5)
    print(c)
except ValueError:
    print('Такого элемента нет')

#5. .pop(i). Удаляет и возвращает элемент по индексу i (по умолчанию удаляет последний)

last = c.pop()
print(last, c)
val = c.pop(5)
print(val, c)


#ind = c.pop(1000)
'''
IndexError: pop index out of range (индекс в pop вышел за границы)
'''
#print(c)

#6. .clear(). Удаляет все элементы из списка. У нас остается пустой список.
d = [1, 2, 3]
d.clear()
print(d)

#Как удалить целиком из памяти объект
del d
#NameError: name 'd' is not defined
#print(d)

#7. .index(x, start = 0, end = len(sp)). Возвращает индекс первого вхождения x в диапазоне [start:end]. Вызывает ValueError, если x нет
print(c.index(2))

#8. .count(x). Подсчитывает количество вхождений x
print(c.count(3))

#9. .sort(key = None, reverse = False). Сортирует список на месте. key - функция для кастомной сортировки. reverse - флажок для сортировок по убыванию/возрастанию (по умолчанию - по возрастанию)

c.sort()
print(c)

c.sort(reverse = True)
print(c)

print(lst)

lst.sort(key = len)
print(lst)

#10. .reverse(). Переворачивает список на месте.
a = c[::-1] #срез для переворота списка. создается новый объект
print(a)

a.reverse()
print(a)

#11. .copy(). Возвращает копию списка
new_a = a.copy() #ссылка на новый объект
print(new_a)

'''
a = [1, 2, 3]
b = a (это отчасти копирование, но ссылается на тот же самый объект)
'''
from copy import deepcopy

p = [[1, 2], [3, 4], [5, 6]]
b = deepcopy(p)
b[0][0] = 0
print(b, p)

p = [[1, 2], [3, 4], [5, 6]]
b = p.copy()
b[0][0] = 0
print(b, p)

'''
copy() - поверхностная копия создает новый составной объект, а затем вставляет в него ссылки на объекты, находящиеся в оригинале

deepcopy() - глубокая копия. создает новый составной объект, и затем рекурсивно вставляет в него копии объектов, находящихся в оригинале
'''

#Преобразование типов

#Из строки в список

s = 'a b c'
print(s.split())

#Из списка в строку
sp = ['a', 'b', 'c']
print(','.join(sp))

#Из других итерируемых объектов
p = 'hello'
print(list(p))
print(list((1, 2, 3)))

lst = [1, 2, 3]
print(str(lst))
print(tuple(lst))

t = list(range(5)) #0, 1 ,2, 3, 4

#Списковые включения

'''
Списковые включения — компактный способ создания списков с использованием выражений.
'''

#Создать список квадратов чисел

y = [x ** 2 for x in t] #при помощи цикла for прохожусь по всем элементам списка t
print(y)
y = [x + 1 for x in t]
print(y)
y = [x // 2 for x in range(6)]
print(y)
y = [x ** 2 for x in t if x % 2 == 0]
print(y)
y = [x ** 2 if x % 2 == 0 else 0 for x in t]
print(y)

#Встроенные функции для списков

#1. len(lst). Возвращает длину списка

lst = [1, 2, 3]
print(len(lst))

#2. sum(lst). Суммирует элементы (для чисел)

print(sum(lst))
lst = [1, 2, 3]

#3. min(lst), max(lst). Находит минимальный/максимальный элемент. Должны быть объекты одного типа данных
#TypeError: '<' not supported between instances of 'str' and 'int'
print(min(lst), max(lst))

#4. sorted(). Создает новый объект (то есть старый неотсортированный сохраняется). Возвращает список.
p = sorted(c, reverse = True)
print(p)

#5. map(func, iterable). Применяет функцию к каждому элементу. Возвращает итератор.
lst = ['13', '454', '67565']
print(list(map(int, lst)))

#6. zip(*iterables). Объединяет элементы из нескольких итерируемых объектов в кортежи

names = ['Alice', 'Bob', 'Henry']
scores = [90, 85]
pairs = list(zip(names, scores))
print(pairs)

'''
Вход: lst = [10, 20, 30, 40]
Задача:

Добавьте число 50 в конец с append().
Замените второй элемент на 25.
Вставьте "new" по индексу 1 с insert().
Проверьте длину списка с len().
'''

lst = [10, 20, 30, 40]
lst.append(50)
lst[1] = 25
lst.insert(1, "new")
print(lst, len(lst))

'''
Вход: lst = ["apple", "banana", "apple", "cherry"]
Задача:

Удалите первое вхождение "apple" с remove().
Удалите последний элемент с pop() и сохраните его.
Проверьте количество "apple" с count().
Выведите в f-строке: f"Список: {lst}, удалён: {popped}, apple count: {count}".
Обработайте ValueError для remove().
'''
lst = ["apple", "banana", "apple", "cherry"]
try:
    lst.remove("apple")
    l = lst.pop()
    print(f"Список: {lst}, удалён: {l}, apple count: {lst.count("apple")}")
except ValueError:
    print("ValueError")

'''
Вход: lst = [5, 2, 8, 2, 1]
Задача:

Найдите индекс первого 2 с index().
Отсортируйте список с sort().
Переверните список с reverse().
'''
lst = [5, 2, 8, 2, 1]
print(lst.index(2))
lst.sort()
lst.reverse()
print(lst)


'''
Вход: lst = [1, 2, 3]
Задача:

Добавьте список [4, 5] с extend().
Вставьте "start" в начало с insert().
Удалите все элементы с clear().
Проверьте длину списка с len().
'''
lst = [1, 2, 3]
lst.extend([4, 5])
lst.insert(0, "start")
lst.clear()
print(len(lst))