# Задание 1. Гласные буквы
# Команде лингвистов понравилось качество ваших программ, поэтому они
# решили заказать функцию для анализатора текста, которая создавала бы
# список гласных букв в нём и считала бы их количество.
# Напишите программу, которая запрашивает у пользователя текст и генерирует
# список гласных букв этого материала (сама строка вводится на русском языке).
# Выведите в консоль сам список и его длину.
# Пример:
# Введите текст: Нужно отнести кольцо в Мордор!
# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
# Длина списка: 9

str1 = input("Введите текст: ")
vowels = 'ауоиэыяюеё'
count = 0
new_str = []

for i in str1:
    if i.lower() in vowels:
        new_str.append(i)
        count += 1
print(f'Список гласных букв: {new_str},\nДлинна списка: {count}')


# Задача 2. Случайные соревнования
# Мы хотим протестировать работу электронной таблицы для участников
# некоторых соревнований. Есть два списка, то есть две команды, по 20
# участников в каждом. В них хранятся очки каждого участника — вещественные
# числа с двумя знаками после точки, например 4.03.
# Член одной команды соревнуется с участником другой команды под таким же
# номером. То есть первый соревнуется с первым, второй — со вторым и так
# далее.
# Напишите программу, которая генерирует два списка участников (по 20
# элементов) из случайных вещественных чисел (от 5 до 10). Для этого найдите
# подходящую функцию из модуля random. Затем сгенерируйте третий список, в
# котором окажутся только победители из каждой пары.
# Пример:
# Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1,
# 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
# Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8,
# 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
# Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8,
# 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]

from random import uniform

lst1 = []
lst2 = []
lst3 = []

for i in range(20):
    rnd = round(uniform(5, 10), 2)
    lst1.append(rnd)
for j in range(20):
    rnd = round(uniform(5, 10), 2)
    lst2.append(rnd)
    
for i in range(len(lst1)):
    if lst1[i] > lst2[i]:
        lst3.append(lst1[i])
    elif lst1[i] < lst2[i]:
        lst3.append(lst2[i])   
print(f'Первая команда: {lst1}\nВторая команда: {lst2}\nПобедители тура: {lst3}')


# Задача 4. Список списков
# Дан многомерный список:
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# Напишите код, который раскрывает все вложенные списки, то есть оставляет
# лишь внешний список. Для решения используйте только list comprehensions.
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

output = [digit for each_list in nice_list 
                for each_list_2 in each_list 
                for digit in each_list_2]
print(output)

# Задача 5. Шифр Цезаря
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква
# заменялась на следующую по алфавиту через K позиций по кругу. Если взять
# русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать,
# буква А станет буквой Г, Б станет Д и так далее.
# Пользователь вводит сообщение и значение сдвига. Напишите программу,
# которая изменит фразу при помощи шифра Цезаря.
# Пример:
# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.

al = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
str1 = input("Введите текст: ")
n = int(input("Введите сдвиг: "))
res_str = []
tmp = ''
for i in str1:
    for j in range(len(al)):
        if i == al[j]:
            if j+n > len(al)-1:
                j = (j + n) - len(al)
                res_str.append(al[j])
            elif j+n <= len(al)-1:
                res_str.append(al[j+n])
    if i == ' ':
        res_str.append(' ')
print(*res_str)            