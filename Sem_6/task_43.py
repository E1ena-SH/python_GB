# 43. Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу 
# образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. 
# Все числа списка находятся на одной строке через пробел.
#       1 2 1 3 4 5 3 4 -> 3
#       1 2 1 3 4 3 1 -> 2

list_1 = list(map(int,input("Введите массив чисел через пробел: ").split()))
list_2 = set(list_1)
count = 0
a = 0
for i in list_2:
    if list_1.count(i) / 2 >= 1:
        a = list_1.count(i) // 2
        # a = list_1.count(i)
        count += a
print(count)