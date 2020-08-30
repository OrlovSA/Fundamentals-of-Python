# Задание № 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.


def input_check(text):
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
    user_number = input_check("Введите время в секундах: ")

    h = user_number // 3600
    m = (user_number % 3600) // 60
    s = (user_number % 3600) % 60

    print(f"Время = {h}:{m}:{s}")
