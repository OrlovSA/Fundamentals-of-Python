# Задание № 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


def input_check(text="Введите число: "):
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

    i = len(user_number)
    numbers_from_among = []

    while i > 0:
        i -= 1
        numbers_from_among.append(int(user_number[i-1]))

    print(f"1 решение.Максимальная цифра из числа {user_number} = {max(numbers_from_among)}")

# Либо:
    user_number = str(input_check())
    numbers_from_among = list(user_number)
    print(f"2 решение. Максимальная цифра из числа {user_number} = {max(numbers_from_among)}")
