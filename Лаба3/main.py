from time import time, sleep
from fd import *
from gendata import *

data_size = [100, 200, 500, 1000, 5000, 10000, 25000, 50000, 100000]
key_name = "Консервированный горошек"


for size in data_size:
    data = []
    hash_table = HashTable()

    generator(size)  # создаем файл с данными
    with open(f'./data_{size}.txt', mode='r', encoding='UTF-8') as database:
        for one_data in database:
            data.append(Product(one_data.strip()))  # переносим данные из файла в массив
            cp = Product(one_data.strip())
            data.append(cp)
            hash_table.insert(cp)

    start = time()
    value = hash_table.find_simple(key_name)
    sleep(0.01)
    end = time()
    print("Простое хэширование: " + "Размер: " + str(size) + ' ' + "Время: " + str(
        end - start - 0.01) + ' ' + "Число коллизий: " + str(hash_table.collisions_simple) + ' ' + str(value.name))

    start = time()
    value = hash_table.find_hard(key_name)
    sleep(0.01)
    end = time()
    print("Сложное хэширование: " + "Размер: " + str(size) + ' ' + "Время: " + str(
        end - start - 0.01) + ' ' + "Число коллизий: " + str(hash_table.collisions_hard) + ' ' + str(value.name) + '\n')
