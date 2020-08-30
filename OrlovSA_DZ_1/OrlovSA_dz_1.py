# Задание № 1
# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.


def input_check(text = "Введите число: "):
    while True:
        try:
            result = int(input(text))
            return result
        except:
            print("Введено не верное значение")


def output_console(number = 5, line = "min"):
    print(number, type(number))
    print(line, type(line))


while True:
    output_console()
    number_user = input_check()
    line_user = input("Введите буквы: ")
    output_console(number_user, line_user)





