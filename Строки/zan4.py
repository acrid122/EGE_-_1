s = 'Hello, world'
s1 = s.upper()
s1 = s1.center(20)
print(s.upper().center(20)) #если хочется применить несколько методов сразу

#Поиск и замена

#10. .count(sub, start = 0, end = len(s)). Количество подстрок sub в строке. Если передаем позиции, то передаем индексы. Регистрозависим.

print(s.count('l'))
print(s.count('l', 0, 5))
print(s.count('o', 4))

#11. .find(sub, start = 0, end = len(s)). Индекс первого вхождения слева. Если передаем позиции, то передаем индексы.

print(s.find('l'))
print(s.find('o', s.find('o') + 1))
print(s.find('l', s.find('l', s.find('l') + 1)))
print(s.find('b')) #если подстроки в строке нет, то выводится -1.

print(s.count('hello')) #подсчитывает количество подстрок hello в строке.

#12. .index(sub, start = 0, end = len(s)). Индекс первого вхождения слева. Если передаем позиции, то передаем индексы.

'''
Тот же самый функционал, что и у .find(), но отличается тем, что при поиске подстроки, которой нет в строке он выдает ошибку ValueError
'''

try:
    print(s.index('b'))
except ValueError:
    print('Такой буквы нет')

#13. .rfind(sub, start = 0, end = len(s)). Индекс первого вхождения справа (последнее слева). Если передаем позиции, то передаем индексы.

print(s.rfind('l')) #индекс выдается не справа налево (-2), а слева направо (10)

#14. .rindex(sub, start = 0, end = len(s)). Индекс первого вхождения справа (последнее слева). Если передаем позиции, то передаем индексы.
'''
Тот же самый функционал, что и у .rfind(), но отличается тем, что при поиске подстроки, которой нет в строке он выдает ошибку ValueError
'''

#15. .replace(old, new, count = -1). Замена подстроки в строке. Третий параметр - количество вхождений слева, который надо поменять.

print(s.replace('l', 'd'))
print(s.replace('l', 'd', 2))
print(s.lower().replace('o', 'a', 1))
print(s.swapcase().rjust(30).replace('D', 'e'))

#16. .translate(table) / str.maketrans(). .maketranse() - метод класса str, который делает таблицу перевода. .translate(table) - метод, который
# применяет данную таблицу к строке.

table = str.maketrans('eld', '123') #такой способ работает так: e -> 1, l -> 2, d -> 3.
print(s.translate(table))

table1 = str.maketrans({
    'e': '1',
    'l': '3',
    'd': '4'
})
print(s.translate(table1))

table2 = str.maketrans('eld', '456', 'o') #третий параметр - удаляемые символы
print(s.translate(table2))

print(s.replace('l', '')) #замена на пустую строку равносильна удалению

t = str.maketrans('od', '89', 'l')
print(s.translate(t))

t1 = str.maketrans('l', '7', 'o')
print(s.translate(t1))

#Проверка префиксов / суффиксов

#17. .startwith(prefix, start = 0, end = len(s)). Начинается ли строк с prefix

print(s.startswith('Hellop')) #Регистрозависимое

print(s.startswith('world', 7))

#18. .endswith(suffix, start = 0, end = len(s)). Начинается ли строк с suffix

print(s.endswith('world')) #Регистрозависимое

#Разделение и объединение

#19. .split(sep = None, maxsplit = -1). Разделяет строку по sep на maxsplit + 1 частей. По умолчанию sep = пробелу.

s2 = 'Hello, world, today, is, the, great, day'
print(s2.split())
print(s2.split('o'))
print(s2.split('o', 1)) #делим только по первой букве 'o'.
print(s.split('l'))

#20. .rsplit(sep = None, maxsplit = -1). Разделяет строку по sep на maxsplit + 1 частей. По умолчанию sep = пробелу. Делит с конца.

print(s.rsplit('o', 1))

#21. .join(iterable). Преобразует итерируемый объект, состоящий из строк, в одну строку.

sp = ['Hello', 'world', 'today']
print(','.join(sp)) #необязательно соединять по какому-то символу (можно по подстроке). в итерируемом объекте должны быть только строки.

#Удаление символов

s = '       Hello          '
s = '!@@@@###! Hello !!'
#22. .lstrip(chars = None). Удаляет символы в начале. По умолчанию удаляет пробелы
print(s.lstrip())
print(s.lstrip('!@#'))

#23. .rstrip(chars = None). Удаляет символы в конце. По умолчанию удаляет пробелы
print(s.rstrip())
print(s.rstrip('!@#'))

#24. .strip(chars = None). Удаляет символы в начале и в конце.
print(s.strip())
print(s.strip('!@#'))

#Проверки (is...) (True/False)

#25. .isalnum(). Проверяет, находятся ли в строке только буквы или цифры.

print(s.isalnum()) #выводит False, так как есть , и пробел

#26. .isalpha(). Проверяет, находятся ли в строке только буквы

print(s.isalpha())

#27. .isdigit(). Проверяет, находятся ли в строке только цифры

print(s.isdigit())

#28. .islower(). Проверят, находится ли вся строка в нижнем регистре

print(s.islower())

#29. .isupper(). Проверят, находится ли вся строка в верхнем регистре

print(s.isupper())

#30. .istitle(). Проверяет, находится ли вся строка в Titlecase

print(s.istitle())

#Форматирование строк: f-строками.

'''
f - строки позволяют взаимодействовать со значениями переменной
'''

age = int(input())
print("Ваш возраст:", age)
print(f"Ваш возраст: {age}") #внутри фигурных скобок - название переменной

s = 'Ваш возраст: ' + str(age) + ' лет'
s1 = f'Ваш возраст: {age} лет'
print(s, s1)

#Сравнение строк
print('s' > '0000000000000000000000') #сравнение строк лексикографическое (сравниваются Unicode-коды), s - 115, 0 - 48. От длины это никак не зависит
print('12345' > '12346') #5 < 6 -> False
s = 'a,b,c'
print(s.split(',')) #.split() делает список

print(','.join(s.split(',')))


s = 'python'
print(s.startswith('py'), s.endswith('on'))

s = "abc123"
print(s.isalpha(), s.isdigit())