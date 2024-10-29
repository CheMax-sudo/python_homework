# Домашнее задание из лекции 1.

# Задача 1
# Найдите сумму цифр трехзначного числа. 

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = (input("Введите трёхначное число: "))
summ = 0
for i in num:
    summ = summ + int(i)
print(f'{num} -> {summ} ({num[0]} + {num[1]} + {num[2]})')


# Задача 2

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе

# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

num_s = int(input("Сколько всего журавликов: "))
digits = num_s//3
petya = int(digits/2)
serg = petya
katya = digits*2
print(f'{num_s} -> {petya} {katya} {serg}')


# Задача 3

# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

ticket = int(input("Введите шестизначный номер билета: "))
sum_onenum = (ticket//100000)+(ticket//10000%10)+(ticket//1000%10)
sum_twonum = (ticket//100%10)+(ticket//10%10)+(ticket%10)
if sum_onenum == sum_twonum:
    print(f'{ticket} -> YES')
else:
    print(f'{ticket} -> NO')

ticket = list(input("Введите шестизначный номер билета: "))
sum_onenum = sum(map(int, ticket[0:3:1]))
sum_twonum = sum(map(int, ticket[3:6:1]))
if sum_onenum == sum_twonum:
    print(f'{''.join(ticket)} -> YES')
else:
    print(f'{''.join(ticket)} -> NO')


# Задача 4

# Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Введите ширину шиколадки в плитках: "))
# m = int(input("Введите длину шоколадки в плитках: "))
# k = int(input("Введите количество плиток которое хотите отломить: "))

if k < n*m:
    if k%n == 0 or k%m == 0:
        print("Yes")
    else:
        print("No")
else:
    print("Ввод не корректен")

# Практическая работа

# Задание 1
 
# Язык математики
# В первый же день на сайте отвалилась формула по расчёту рекламной
# метрики, и только Вася может её поправить. Часть программы с вводными
# данными представлена ниже, отдельно записана формула на математическом
# языке.
# Дана программа:
# a = 8
# b = 10
# c = 12
# d = 18
# Продолжите программу: переведите выражение с математического языка на
# язык Python, запишите его в переменную res и выведите результат.
  
a = 8
b = 10
c = 12
d = 18  
res = ((-3+a**2)*b-2**3)/(c-2*d)
print(res)


# Задача 2

# Часы
# Напишите программу, которая получает на вход число n (количество минут),
# затем считает, сколько это будет в часах и сколько минут останется, и выводит
# на экран эти два результата.

n = int(input("Введите количество минут: ")) 
hours = n//60
minuts = n%60 
print(f'Часы: {hours} Минуты: {minuts}') 

# Задача 3

# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

ticket = int(input("Введите шестизначный номер билета: "))
sum_onenum = (ticket//100000)+(ticket//10000%10)+(ticket//1000%10)
sum_twonum = (ticket//100%10)+(ticket//10%10)+(ticket%10)
if sum_onenum == sum_twonum:
    print(f'{ticket} -> YES')
else:
    print(f'{ticket} -> NO')

ticket = list(input("Введите шестизначный номер билета: "))
sum_onenum = sum(map(int, ticket[0:3:1]))
sum_twonum = sum(map(int, ticket[3:6:1]))
if sum_onenum == sum_twonum:
    print(f'{''.join(ticket)} -> YES')
else:
    print(f'{''.join(ticket)} -> NO')  


# Задача 4

# Площадь прямоугольного треугольника
# Прямоугольный треугольник — это треугольник, один из углов которого
# является прямым (90 градусов). У прямоугольного треугольника два катета,
# которые образуют прямой угол, и гипотенуза, противоположная этому углу.
# Вам требуется написать программу, которая запрашивает у пользователя
# длины двух катетов и выводит площадь треугольника.
# Площадь прямоугольного треугольника вычисляется по формуле: где a и b — длины катетов, а S — площадь.

a = int(input("Введите длину первого катета: "))
b = int(input("Введите длину второго катета: "))
s = 1/2*a*b
print("Площадь прямоугольного треугольника:",s)


# Задача 5*

# Поменять местами: не всё так просто! (необязательная,
# повышенной сложности)
# Напишите программу, которая меняла бы значения двух переменных местами,
# но без использования третьей переменной и синтаксического сахара, который
# мы разбирали, а именно: без конструкции a, b = b, a. В переменные будут
# вводиться только числа.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

# Изменять, удалять, менять местами первую, вторую, третью и последнюю
# строчки нельзя. В четвёртую строку можно вставлять сколько угодно кода, не
# трогая последний print.

