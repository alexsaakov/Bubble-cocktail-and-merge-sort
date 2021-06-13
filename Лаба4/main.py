from datetime import datetime
from statistic import *
from time import time, sleep
import random

def random_number():
    return datetime.now().microsecond

def lkm(m, k, b, r0):
    return (k * r0 + b) % m

def mmp(r0, r1):
    return int(str(r0 * r1)[0:4])

list_lkm = [[], [], [], [], [], [], [], [], [], []]
list_mmp = [[], [], [], [], [], [], [], [], [], []]

m = 2 ** 31 - 1
k = 1452755321
b = 13

for j in range(10):
    r0 = random_number() % 100
    sleep(0.01)
    for i in range(50):
        r1 = lkm(m, k, b, r0) % 10000
        r0 = r1
        list_lkm[j].append(r1)


z0 = random_number()
for j in range(10):
    z1 = random_number()
    for i in range(50):
        z2 = mmp(z0, z1) % 10000
        z0 = z1
        z1 = z2
        list_mmp[j].append(z2)


avg_mmp = []
avg_lkm = []
dispersion_mmp = []
dispersion_lkm = []
variation_coefficient_mmp = []
variation_coefficient_lkm = []
chi_square_mmp = []
chi_square_lkm = []

for list in list_lkm:
    avg_lkm.append(avg(list))
    dispersion_lkm.append(dispersion(list))
    variation_coefficient_lkm.append(variation_coefficient(list))
    chi_square_lkm.append(chi_square(list))

print("Линейный конгруэнтный метод:")
print("Среднее:", avg_lkm)
print("Дисперсия:", dispersion_lkm)
print("Коэффициент вариации:", variation_coefficient_lkm)
print("Равномерность распределения и случайность, используя критерий Хи-квадрат:", chi_square_lkm)

for list in list_mmp:
    avg_mmp.append(avg(list))
    dispersion_mmp.append(dispersion(list))
    variation_coefficient_mmp.append(variation_coefficient(list))
    chi_square_mmp.append(chi_square(list))

print("Метод серединных произведений:")
print("Среднее:", avg_mmp)
print("Дисперсия:", dispersion_mmp)
print("Коэффициент вариации:", variation_coefficient_mmp)
print("Равномерность распределения и случайность, используя критерий Хи-квадрат:", chi_square_mmp)

size = [1000, 10000, 50000, 100000, 150000, 500000, 800000, 1000000]

for value in size:
    print("Размер " + str(value) + ":")
    start = time()
    r0 = random_number() % 100
    for i in range(value):
        r1 = lkm(m, k, b, r0) % 10000
        r0 = r1
    sleep(0.01)
    end = time()
    print("Время линейным конгруэнтным методом " + str(end - start - 0.01))

    start = time()
    z0 = random_number()
    z1 = random_number()
    for i in range(value):
        z2 = mmp(z0, z1) % 10000
        z0 = z1
        z1 = z2
    sleep(0.01)
    end = time()
    print("Время методом серединных произведений " + str(end - start - 0.01))

    start = time()
    for i in range(value):
        random.uniform(0, 10000)
    sleep(0.01)
    end = time()
    print("Время встроенным методом " + str(end - start - 0.01))
