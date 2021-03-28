class Product:  # класс сотрудник
    name: str
    country: str
    volume: str
    price: str

    def __init__(self, line: str):  # инициализация
        name, country, volume, price = line.split(', ')
        self.name = name
        self.country = country
        self.volume = volume
        self.price = price

    def __lt__(self, other):  # Перегрузка оперптора <
        if isinstance(other, str):
            if self.name < other:
                return True
            else:
                return False
        else:
            if self.name < other.name:
                return True
            else:
                return False

    def __le__(self, other):  # Перегрузка оператора <=
        if isinstance(other, str):
            if self.name <= other:
                return True
            else:
                return False
        else:
            if self.name <= other.name:
                return True
            else:
                return False

    def __gt__(self, other):  # Перегрузка оператора >
        if isinstance(other, str):
            if self.name > other:
                return True
            else:
                return False
        else:
            if self.name > other.name:
                return True
            else:
                return False

    def __ge__(self, other):  # Перегрузка оператора >=
        if isinstance(other, str):
            if self.name >= other:
                return True
            else:
                return False
        else:
            if self.name >= other.name:
                return True
            else:
                return False

    def __eq__(self, other):  # Перегрузка оператора ==
        if isinstance(other, str):
            if self.name == other:
                return True
            else:
                return False
        else:
            if self.name == other:
                return True
            else:
                return False


def simple_find(array, key):
    res = -1
    for i in range(len(array)):
        if array[i].name == key:
            res = i
            # можешь тут поставить break, если хочешь. тогда будет быстрее работать, но график будет некрасивый =)
    if res == -1:
        return 'not found'
    return res


def binary_find(array, key):
    mid = len(array) // 2
    mn = 0
    mx = len(array) - 1

    while array[mid].name != key and mn <= mx:
        if array[mid].name < key:
            mn = mid + 1
        else:
            mx = mid - 1
        mid = (mn + mx) // 2
    if mn <= mx:
        return mid
    else:
        return 'not found'


class MultimapProduct:
    key: list
    value: list

    def __init__(self, array):  # инициализация
        self.key = []
        self.value = []

        for product in array:
            self.key.append(product.name)
            self.value.append(product)

    def insert(self, product):
        self.key.insert(self.find(product.name), product.name)
        self.value.insert(self.find(product), product)

    def find(self, key):
        mid = len(self.key) // 2
        mn = 0
        mx = len(self.key) - 1

        while self.key[mid] != key and mn <= mx:
            if self.key[mid] < key:
                mn = mid + 1
            else:
                mx = mid - 1
            mid = (mn + mx) // 2
        if mn <= mx:
            return mid
        else:
            return 'not found'
