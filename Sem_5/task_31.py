# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0  = 0, a1  = 1, ak  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
#     Input: 7
#     Output: 21

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1)+fib(n-2)

list = []
for i in range(1,21):
    list.append(fib(i))
print(list)
print(fib(19))