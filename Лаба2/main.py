from time import sleep, time
from gendata import *
from sorts import merge_sort
from fd import *

data_size = [10000, 20000, 50000, 100000, 150000, 250000, 500000, 800000, 1000000]

for size in data_size:
    data = []
    generator(size)  # создаем файл с данными
    with open(f'./data_{size}.txt', mode='r', encoding='UTF-8') as database:
        for one_data in database:
            data.append(Product(one_data.strip()))  # переносим данные из файла в массив

    key = data[random.randint(0, len(data) - 1)].name

    start = time()
    simple_find(data, key)
    sleep(0.001)
    end = time()
    simple_find_time = str(end - start - 0.001)

    start = time()
    merge_sort(data)
    binary_find(data, key)
    sleep(0.001)
    end = time()
    binary_find_time = str(end - start - 0.001)

    start = time()
    binary_find(data, key)
    sleep(0.001)
    end = time()
    binary_find_and_sort_time = str(end - start - 0.001)

    data_multimap = MultimapProduct(data)
    start = time()
    data_multimap.find(key)
    sleep(0.001)
    end = time()
    multimap_time = str(end - start - 0.001)

    print("size = " + str(size))
    print("время прямого поиска = " + simple_find_time)
    print("время сортировки массива слиянием и бинарный поиск в нем = " + binary_find_time)
    print("время бинарного поиска для заранее отсортированного массива = " + binary_find_and_sort_time)
    print("время поиска в multimap = " + multimap_time)
