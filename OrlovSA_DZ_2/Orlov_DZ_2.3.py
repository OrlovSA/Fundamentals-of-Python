#  3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# # относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

seasons = {
    1: ["Зима", 'Январь'],
    2: ["Зима", 'Февраль'],
    3: ["Весна", 'Март'],
    4: ["Весна", 'Апрель'],
    5: ["Весна", 'Май'],
    6: ["Лето", 'Июнь'],
    7: ["Лето", 'Июль'],
    8: ["Лето", 'Август'],
    9: ["Осень", 'Сентябрь'],
    10: ["Осень", 'Октябрь'],
    11: ["Осень", 'Ноябрь'],
    12: ["Зима", 'Декабрь']
}


def input_check(text):
    while True:
        try:
            result = int(input(text))
            if result <= 0:
                print("Число меньше или ровно 0")
            elif result > 12:
                print("Число больше 12")
            else:
                return result
        except ValueError:
            print("Введено не верное значение")


month = input_check("Введите Месяц от 1 - 12: ")
print(f'{month}й месяц {seasons.get(month)}.')