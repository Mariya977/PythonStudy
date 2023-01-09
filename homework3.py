# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# my_list = [1,2,3,4,5,6,7,9]
# sum = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         sum += my_list[i]
# print(sum)

# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def mult_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)

# lst = [2, 3, 4, 5, 6]
# mult_lst(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_lst(lst)

# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# my_list = list(map(float, input("Введите числа через пробел:\n").split()))
# new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
# print(max(new_list) - min(new_list))

# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# final_num = " "
# num = int(input('Введите число: '))
# while num != 0:
#     final_num = str(num % 2) + final_num
#     num //= 2
# print(final_num)

# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def findFib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return findFib(index-1) + findFib(index-2)


n = int(input('Введите число: '))
my_list = [findFib(i) for i in range(1, n+2)]
my_list = my_list[::-1] + my_list[1:]
print(my_list)