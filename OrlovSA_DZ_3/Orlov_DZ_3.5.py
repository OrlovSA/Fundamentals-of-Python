# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
# завершить программу.gfd


def list_formation():
    """Создаем список из входящих данных"""
    while True:
        result = input("Введите цифры через пробел: ").split()
        if len(result) == 0:
            print("Нет данных")
        else:
            return result


def numbers_init_symbols(symbols):
    """Ищим в строке Цифры"""
    result = "0"
    for i in symbols:
        if i.isdigit():
            result += (i)
    return result


result = 0
flag = True
while flag:
    for i in list_formation():
        if i.isdigit():
            result += int(i)
        elif i.isalnum():
            result += int(numbers_init_symbols(i))
            flag = False
        else:
            flag = False
    print(result)
else:
    print("программы завершается.")

