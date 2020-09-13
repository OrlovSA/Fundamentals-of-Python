# 5) Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут t itle
# (название) и метод draw ( отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title
        print(title)

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручки.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркера.')


result_1 = Pen('Ручка')
result_1.draw()
result_2 = Pencil('Карандаш')
result_2.draw()
result_3 = Handle('Маркер')
result_3.draw()