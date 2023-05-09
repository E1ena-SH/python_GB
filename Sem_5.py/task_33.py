# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
#     Input: 5 -> 1 3 3 3 4
#     Output: 1 3 3 3 1


def max_min(N):
    from random import randint
    list = [randint(1, 5) for i in range(N)]
    print(list)
    a = max(list)
    
    for i in range(len(list)):
        if list[i] == a:      
            list[i] = min(list)
    print(list)

max_min(8)
