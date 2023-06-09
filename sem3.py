# ------Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
#   Input: [1, 1, 2, 0, -1, 3, 4, 4]
#   Output: 6

# Примечание:   Пользователь может вводить значения
#               списка или список задан изначально.

# nums = [1, 2, 3, 4, 1, 2]
# print(set(nums))
# print(len(set(nums)))

# uniq = [i for i in nums if nums.count(i) == 1]
# print(uniq)


# -------Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
#       Input: [0, -1, 5, 2, 3]
#       Output: 2 (-1 < 5, 2 < 3)
# Примечание:   Пользователь может вводить значения
#               списка или список задан изначально.

# nums = [1, 2, 3, 1, 2, 4, 1]
# count = 0

# for i in range(len(nums)):
#     if nums[i] > nums[i-1]:
#         count += 1
# print(count)

# #  ВТОРОЙ ВАРИАНТ решения этой задачи:
# result = [nums[i] for i in range(1, len(nums)) if nums[i] > nums[i-1]]
# print(len(result)) 


# -------Задача №19. Общее обсуждение
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
#       Input: [1, 2, 3, 4, 5] k = 3
#       Output: [4, 5, 1, 2, 3]


nums = [1, 2, 3, 4, 5]
k = int(input('Введите число k: '))
i = 0

while i < k:
    nums.append(nums[0])
    nums.pop(0)
    
    i += 1
print(nums)
print(nums[k:] + nums[:k]) # вывод на печать без разделителей

