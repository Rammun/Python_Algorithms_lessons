# 1. Пользователь вводит данные о количестве предприятий, их наименования
#  и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
#  Программа должна определить среднюю прибыль (за год для всех предприятий)
#  и вывести наименования предприятий, чья прибыль выше среднего и отдельно
#  вывести наименования предприятий, чья прибыль ниже среднего.

class Company:
    def __init__(self, name):
        self._name = name
        self._profits = []
        self._total_profit = 0

    @property
    def name(self):
        return self._name

    @property
    def profits(self):
        return self._profits

    @property
    def total_profit(self):
        return self._total_profit

    def add_profit(self, profit):
        self._profits.append(profit)
        self._total_profit += profit

number = int(input("Введите кол-во компаний: "))
companies = [None] * number

for n in range(number):
    company_name = input(f"{n + 1}. Введите название компании: ")
    company = Company(company_name)

    for quarter in range(4):
        profit = int(input(f"прибыль за {quarter + 1} квартал: "))
        company.add_profit(profit)

    companies[n] = company
    print()

average_profit = sum([p.total_profit for p in companies]) / len(companies)

print(f"Средняя прибыль за год всех компаний: {average_profit}\n")

print("Компании с прибылью ниже среднего:")
for comp in companies:
    if(comp.total_profit < average_profit):
        print(f"{comp.name}: {comp.total_profit}")

print("Компании с прибылью выше среднего:")
for comp in companies:
    if(comp.total_profit > average_profit):
        print(f"{comp.name}: {comp.total_profit}")


