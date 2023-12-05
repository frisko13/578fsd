Задание 1:
num1 = float(input("Введите первое число: "))
oper = input("Введите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if oper == "+":
    result = num1 + num2
elif oper == "-":
    result = num1 - num2
elif oper == "*":
    result = num1 * num2
elif oper == "/":
    result = num1 / num2

print("Результат выражения:", result)

Задание 2:
import random


num_list = [random.randint(-10, 10) for i in range(10)]
print("Исходный список:", num_list)

min_num = min(num_list)
max_num = max(num_list)
print("Минимальный элемент:", min_num)
print("Максимальный элемент:", max_num)


neg_count = 0
pos_count = 0
zero_count = 0
for num in num_list:
    if num < 0:
        neg_count += 1
    elif num > 0:
        pos_count += 1
    else:
        zero_count += 1

print("Количество отрицательных элементов:", neg_count)
print("Количество положительных элементов:", pos_count)
print("Количество нулей:", zero_count)
