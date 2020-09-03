# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

user_out = lambda name, surname, date_birth, city, email, number: print(name, surname, date_birth, city, email, number)


user_out(
    name=input("Введите Имя: "),
    surname=input("Введите Фомилию: "),
    date_birth=input("Введите год рождения: "),
    city=input("Введите город: "),
    email=input("Введите email: "),
    number=input("Введите телефон: ")
)



