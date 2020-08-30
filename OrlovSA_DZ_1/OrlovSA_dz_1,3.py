# Задание № 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.


def input_check(text = "Введите число: "):
    while True:
        try:
            result = int(input(text))
            if result <= 0:
                print("Число меньше или ровно 0")
            else:
                return result
        except:
            print("Введено не верное значение")


while True:
    user_number = str(input_check())

    n2 = user_number + user_number
    n3 = n2 + user_number

    user_number = int(user_number)
    n2 = int(n2)
    n3 = int(n3)

    user_number = user_number + n2 + n3

    print(user_number)