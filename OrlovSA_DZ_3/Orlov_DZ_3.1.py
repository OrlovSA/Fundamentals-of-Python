#1)  Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.


def input_check(text):
    """Проверяем на число"""
    while True:
        try:
            result = int(input(text))
            return result
        except ValueError:
            print("Введено неверное значение")


def division(number_1, number_2):
    """Проверяем деление на 0"""
    while True:
        try:
            return number_1 / number_2
        except ZeroDivisionError:
            print('division by zero')
            number_2 = input_check(f"Ведите делитель числа: {number_1} / ")


user_number_1 = input_check("Ведите делимое число: ")
user_number_2 = input_check(f"Ведите делитель числа: {user_number_1} / ")

print(round(division(number_1=user_number_1, number_2=user_number_2), 2))

