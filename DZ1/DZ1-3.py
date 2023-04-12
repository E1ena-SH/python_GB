# -------Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*       385916 -> yes
#                 123456 -> no
#                 001001 -> yes

T = int(input())
sum_1 = 0
sum_2 = 0

for i in range(1,4):
    b = T % 10 
    sum_1 = sum_1 + b
    T =T//10

for i in range(4,7):
    b = T % 10 
    sum_2 = sum_2 + b
    T =T//10

if sum_1 == sum_2: print('YES')
else: print('NO')
