# 39. Даны два массива чисел. 
# Требуется вывести те уникальные элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. 
# Элементы обоих массивов вводятся в две строки через пробел.

# Пример:         1 2 3 4 5 6
#                 4 5 6 7 8 -> 1 2 3

list_1 = list(map(int,input("Введите массив чисел через пробел: ").split()))
list_2 = list(map(int,input("Введите массив чисел через пробел:  ").split()))
a = set(list_1)
b = set(list_2)
print(a.difference(b))
print([int(i) for i in list_1 if i not in list_2])