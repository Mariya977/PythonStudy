## 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# def sum_digits(my_num):
#     return sum(map(int, my_num.replace('.', ' ').replace('-',' ')))

# print('Введите число ')
# my_num = (input())
# print(f'Сумма цифр в {my_num} равна {sum_digits(my_num)}')

## 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int(input('Введите число N '))

# x = 1
# for i in range(N):
#     i += 1
#     x *= i
#     print(x, end=" ")

## 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# my_num = int(input('Введите n (кол-во чисел в списке) '))
# sum = 0
# my_list = {i : 3*i + 1 for i in range(1, my_num+1)}
# print(f'Для n = {my_num}: {my_list}')

# def chain(my_num):
#     return[round((1 + 1 / i)**i, 2) for i in range (1, my_num + 1)]
# print(f'Список для {my_num} чисел =', chain(my_num))

# for i in range(1, my_num + 1):
#     sum += (1 + 1 / i) ** i
# print(f'Сумма последовательности из {my_num} чисел равна: {sum}')


## 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

## Не смогла решить(((


## 5. Реализуйте алгоритм перемешивания списка.

import random
my_list = [random.randint(0, 10) for i in range(random.randint(5, 20))]
print(my_list)
random.shuffle(my_list)
print(my_list)