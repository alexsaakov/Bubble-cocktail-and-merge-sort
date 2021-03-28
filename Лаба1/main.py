import copy
from gendata import generator
from sorts import bubble_sort, cocktail_sort, merge_sort
from datetime import datetime
from product_class import Product


data_size = [100, 200, 500, 1000, 5000, 10000, 50000, 100000]

for size in data_size:
    data = []
    generator(size)  # создаем файл с данными
    with open(f'./data_{size}.txt', mode='r', encoding='UTF-8') as database:
        for one_data in database:
            data.append(Product(one_data.strip()))  # переносим данные из файла в массив

    data_bubble = copy.deepcopy(data)
    data_cocktail = copy.deepcopy(data)
    data_merge = copy.deepcopy(data)

    start1 = datetime.now()
    bubble_sort(data_bubble)  # сортировка пузырьком
    end1 = datetime.now()

    start2 = datetime.now()
    cocktail_sort(data_cocktail)  # шейкер-сортировка
    end2 = datetime.now()

    start3 = datetime.now()
    merge_sort(data_merge)  # сортировка слиянием
    end3 = datetime.now()

    print(str(size) + 'bubble sort:' + str(end1 - start1) + '\n')
    print(str(size) + 'cocktail sort:' + str(end2 - start2) + '\n')
    print(str(size) + 'merge sort:' + str(end3 - start3) + '\n')
    
    with open('./time.txt', mode='a', encoding='UTF-8') as result:
        result.write(f"size: {size} bubble sort: {str(end1 - start1)}" + '\n')
        result.write(f"size: {size} cocktail sort: {str(end2 - start2)}" + '\n')
        result.write(f"size: {size} merge sort: {str(end3 - start3)}" + '\n')
