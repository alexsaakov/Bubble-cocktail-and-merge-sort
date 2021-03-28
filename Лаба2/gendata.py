import random


data_name = ['рыба', 'хлеб', 'масло', 'яблоки', 'груши', 'зерно', 'шоколад']
data_country = ['США', 'Китай', 'Германия', 'Австрия', 'Венгрия', 'Аргентина', 'Австралия', 'Перу']
data_volume = ['1 тонна', '2 тонны', '5 тонн', '10 тонн', '15 тонн', '20 тонн', '30 тонн', '50 тонн']
data_price = ['500000 рублей', '1000000 рублей', '1250000 рублей', '14850000 рублей', '12340000 рублей', '7050000 рублей']


def generator(size):
    res = []
    for i in range(size):
        product = ''
        product += data_name[random.randint(0, len(data_name) - 1)] + ', '
        product += data_country[random.randint(0, len(data_country) - 1)] + ', '
        product += data_volume[random.randint(0, len(data_volume) - 1)] + ', '
        product += data_price[random.randint(0, len(data_price) - 1)]
        res.append(product)

    with open(f'./data_{size}.txt', mode='w', encoding='UTF-8') as data_product:
        for one_product in res:
            data_product.write(f"{one_product}" + '\n')  # записываем один элемент в файл
