"""Консольная программа для оформления отчёта об эксперименте.

Запрашивает у пользователя имя исследователя, название эксперимента,
количество запусков, длительность одного запуска и два вещественных
числа — действительную и мнимую части комплексного коэффициента.
Выводит карточку эксперимента и диагностическую строку с типами
всех введённых значений.
"""

name_us = input("Ваше имя: ")
name_exp = input("Название эксперимента: ")
countruns = int(input("Количество выполненных запусков: "))
time = float(input("Длительность запуска в секундах: "))
print("Действительная и мнимая часть комплексного коэффициента - (два вещественных числа): ")
c1 = float(input())
c2 = float(input())

compl = complex(c1, c2)
timesec = time * countruns
complsq = compl.real ** 2 + compl.imag ** 2


out1 = f"ЭКСПЕРИМЕНТ: {name_exp}"
out2 = f"Исследователь: {name_us}"
out3 = f"Запуски: {countruns}"
out4 = f"Общее время: {timesec:.2f} с ({timesec/60:.2f})"
out5 = f"Коэффициент: ({compl.real}, {compl.imag}j)"
out6 = f"Квадрат модуля: {complsq:.2f}"
out7 = f"Есть выполненные запуски: {bool(countruns)}"

len_symb = max(len(out1), len(out2), len(out3), len(out4), len(out5), len(out6), len(out7))

print("=" * len_symb)
print(out1)
print(out2)
print(out3)
print(out4)
print(out5)
print(out6)
print(out7)
print("=" * len_symb)


print()
print("Типы введённых значений:")
print("name_us:", type(name_us))
print("name_exp:", type(name_exp))
print("countruns:", type(countruns))
print("time:", type(time))
print("c1:", type(c1))
print("c2:", type(c2))