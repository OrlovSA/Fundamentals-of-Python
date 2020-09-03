# 4) Программа принимает действительное положительное число x и целое отрицательное число
# y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.


def input_check_x(text):
    """Проверяем на положительное число"""
    while True:
        try:
            x = int(input(text))
            if x <= 0:
                print("Число не положительное")
            else:
                return x
        except ValueError:
            print("Введены символы.")


def input_check_y(text):
    """Проверяем на отрицательное число"""
    while True:
        try:
            y = int(input(text))
            if y >= 0:
                print("Число не отрицательное")
            else:
                return y
        except ValueError:
            print("Введены символы.")


def my_func(x, y):
    """Возведение в степени"""
    print(f'Вариант №1: {round(x**y, 4)}')
    result = x * x
    for i in range(2, abs(y)):
        result = result * x
    print('Вариант №2:', round(1 / result, 4))


my_func(input_check_x("Введите действительное положительное число: "), input_check_y("Введите целое отрицательное число: "))