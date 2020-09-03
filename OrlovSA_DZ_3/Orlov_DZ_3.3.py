# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.


def input_check(text):
    """Проверяем на число"""
    while True:
        try:
            result = int(input(text))
            return result
        except ValueError:
            print("Введено неверное значение")


def my_func(x, y, n):
    """Вычисляем 2 наибольших числа и суммируем"""
    numbers = []
    numbers.extend([x, y, n])
    numbers.sort()
    return numbers[1] + numbers[2]


number_1 = input_check("Введите число №1: ")
number_2 = input_check("Введите число №2: ")
number_3 = input_check("Введите число №3: ")

print(my_func(x=number_1, y=number_2, n=number_3))
