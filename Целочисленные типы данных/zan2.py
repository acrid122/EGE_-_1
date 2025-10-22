'''
int - integer (целые числа). Целочисленный тип данных. Числа, у которых нет дробной части. 5, -10, 0, 10000000000000000000000000.
Маленькие int (-5 до 256) хранятся в памяти один раз для оптимизации. (кэширование)
'''
x = 3.5
print(int(x)) #остается только целая часть.

y = 3
print(float(y)) #3.0 тип float

'''
float - число с плавающей точкой (вещественное число). Точность ограничена (около 15 знаков) из-за представления в памяти. 
'''
z = 3.5
z = 1.0
z = -0.5
z = 2.5e-3 #(0.0025)
z = .589347589347
print(z)

print(0.1 + 0.2 == 0.3) #неточная точнось, это связано со способом представления вещественных чисел в памяти

'''
complex - комплексные числа. Это число, состоящее из двух частей: реальной (действительной) и мнимой. z = a + bi.
'''
p = 2 + 3j
print(p)
print(p.real, p.imag)

#print(help(int)) #ф-ия help помогает вспомнить все методы, описанные внутри класса

#Арифметические операции
'''
+ - сложение
- - вычитание
/ - деление
* - умножение
% - остаток от деления
// - целочисленное деление
** - возведение в степень
'''

#PEMDAS - приоритет арифметических операций
'''
P - Parentheses (скобки)
E - Exponents (вовзедение в степень)
M - Multiplication (умножение)
D - Division (деление)
A - Addition (сложение)
S - Subtraction (вычитание)
'''
'''
1. ()
2. **
3. унарный +, -
4. *, /, //, %
5. +, -
'''

#Процесс создания калькулятор

import math #при таком импорте всегда прописываем имя модуля перед используемой функцией или классом.
print(math.sqrt(6))
'''
from math import * #* - импорт абсолютно всего
print(sqrt(6))

from math import sqrt, isqrt #перечисление через запятую того функционала, который нужен

import matplotlib as mpl #сокращение названия модуля для более удобного использования
print(m.get_data_path)
'''

#print(help(math))

while True:
    try:
        num1 = float(input("Первое число (или 'exit' для выхода): ")) #float() - для преобразования к вещественному числу. input() - выдает строковый результат
        num2 = float(input('Второе число: '))
    except ValueError:
        print('Неверный ввод!')
        continue

    operation = input('Действие (+, - , *, /, //, %, **, sqrt, sin, cos, log, ln, exp, fact): ')

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print('Делить на ноль нельзя!!!')
        else:
            print(num1 / num2)
    elif operation == "//":
        if num2 == 0:
            print('Делить на ноль нельзя!!!')
        else:
            print(num1 // num2)   
    elif operation == "%":
        if num2 == 0:
            print('Делить на ноль нельзя!!!')
        else:
            print(num1 % num2)     
    elif operation == "**":
        print(num1 ** num2)
    elif operation == 'sin':
        print(math.sin(num1))
    elif operation == 'cos':
        print(math.cos(num1))
    elif operation == 'sqrt': #isqrt - корень, но только целая его часть
        print(math.sqrt(num1))
    elif operation == 'log':
        print(math.log(num2, num1))
    elif operation == 'ln':
        print(math.ln(num1))    
    elif operation == 'exp':
        print(math.exp(num1)) 
    elif operation == 'fact':
        print(math.fact(int(num1))) 
    else:
        print('Неизвестное действие')

    if input("Продолжить? (да/нет): ") == 'нет':
        break

'''
Остатки от отрицательных чисел:

-7 % 3 = 2
7 % 3 = 1
3 - 1 = 2 - остаток от отрицательного числа


-9 % 4 = 3.
'''

'''
round() - математическое округление
'''

print(round(1.5)) #Округление происходит в сторону четного, если число равноудалено от двух целых.
print(round(10.51))
print(round(10.513, 2)) #второй параметр - округление до количества знаков

'''
divmod() - возвращает кортеж, содержащий частное и остаток.
'''

print(divmod(-9, 4))

'''
pow() - возводить в степень
'''
print(pow(2, 3, 2))