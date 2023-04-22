# -------Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#     *Пример:*       5
#                     1 2 3 4 5
#                     6
#                     -> 5

N = int(input('Введите число N:  '))
list = []
x = int(input('Введите число X:  '))
min = x
number = 0
import random

for i in range(N):
    list.append(random.randint(1,10))
    if min > abs(x - list[i]):
        min = abs(x - list[i])
        number = list[i]
print(list)
print(number)
        

