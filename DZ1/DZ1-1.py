# ----------- Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#     123 -> 6 (1 + 2 + 3)
#     100 -> 1 (1 + 0 + 0)

a = int(input('Введите трехзначное число:  '))
sum = 0
b = 0
if 99 < a < 1000:
    while a > 0:
        b = a % 10 
        sum = sum + b
        a =a//10
    print(sum)
else:
    print("Неверное число")