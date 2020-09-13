# 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.
import json


def read_file():
    try:
        with open("text5.7.txt") as f:
            for i in f:
                i = i.strip()
                yield i.split()
    except IOError:
        print("Произошла ошибка")


profits = {'average_profit': 0}
firm_prof = {}
damages = {}
result = []
for i in read_file():
    profit = 0
    if int(i[2]) > int(i[3]):
        profit += int(i[2]) - int(i[3])
        x = profits.get('average_profit') + profit
        profits.update({'average_profit': x})
        firm_prof.update({i[0]: profit})
    else:
        profit += int(i[2]) - int(i[3])
        damages.update({i[0]: profit})
else:
    x = profits.get('average_profit') / len(firm_prof)
    profits.update({'average_profit': round(x, 2)})
    firm_prof.update(damages)
    result.append(firm_prof)
    result.append(profits)


with open("json5.7.json", "w") as f:
    json.dump(result, f)
    print('Json dump = ' + json.dumps(result))