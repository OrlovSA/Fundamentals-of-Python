# 3) Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
# surname, position ( должность), i ncome ( доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
# дохода с учетом премии ( get_total_income) . Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# # вызвать методы экземпляров).


class Worker:
    def __init__(self, name="Вася", surname='Пупкин', position='Инженегр'):
        self.name = name
        self.surname = surname
        self.position = position
        self._ncome = {"wage": 85000, "bonus": 25000}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname} {self.position}')


    def get_total_income(self):
        print(int(self._ncome.get("wage")) + int(self._ncome.get("bonus")))


result_1 = Position()
result_1.name = 'Вова'
result_1.surname = 'Сусликов'
result_1.position = 'протаптыватель тропинок'
result_1.get_total_income()
result_1.get_full_name()