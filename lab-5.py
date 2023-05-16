# Задана рекуррентная функция. Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
# 15.F(0) = 1, F(1) = 1, F(n) = 2*F(n–1) + F(n-2), при n > 1
from timeit import timeit
import matplotlib.pyplot as plt

a = []
b = []


def paf(w):  # Итерация
    if w == 0:
        return 1
    if w == 1:
        return 1
    if w > 1:
        return 2 * paf(w - 1) + paf(w - 2)


def pav(n):  # Рекурсия
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        f = [1] * 4
        f[1] = 1
        f[2] = 1
        for i in range(2, n + 1):
            f[3] = 2 * f[2] + f[1]
            f[0], f[1], f[2] = f[1], f[2], f[3]
        return f[3]


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(paf(i))
try:
    print(paf(1000))
except:
    print('При вводе 1000 для функции вычисляемой рекурсивно, значение слишком велико и выдаёт ошибку')
print('')
try:
    print("При вводе 1000 для функции, вычисляемой итеративно, получаем следующее значение")
    print(str(pav(1000)))
except:
    print("Ошибка")
print('')
print('№' + '       ' + 'Рекурсивно' + '        ' + 'Итеративно')
for i in range(1, 11):
    stp1 = 'from __main__ import paf'
    stmt_i = 'paf(' + str(i) + ')'
    stp2 = 'from __main__ import pav'
    stmt_j = 'pav(' + str(i) + ')'
    a.append(timeit(setup=stp1, stmt=stmt_i, number=20000))
    b.append(timeit(setup=stp2, stmt=stmt_j, number=20000))
    print(str(i) + '|' + str(round(timeit(setup=stp1, stmt=stmt_i, number=20000), 17)) + '|' + str(
        round(timeit(setup=stp2, stmt=stmt_j, number=20000), 17)))
y1 = a
y2 = b
plt.xlabel('Число, которое подаётся')
plt.ylabel('Время поиска')
plt.plot(x, y1, label='Рекурсивно')
plt.plot(x, y2, label='Итеративно')
plt.legend()
plt.show()
