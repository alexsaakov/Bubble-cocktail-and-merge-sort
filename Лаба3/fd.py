MAXSIZE = 200 # так мало, чтобы коллизии были


def simple_hash(key):
    _hash = 0
    for i in key:
        _hash += ord(i)
    return _hash % MAXSIZE


def hard_hash(key):
    _hash = 0
    for i in key:
        _hash += ord(i)
        _hash -= (_hash << 13) | (_hash >> 19)
    return _hash % MAXSIZE


def get_new_pos(old_hash):
    return (old_hash + 1) % MAXSIZE


class Product:
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
        self.hash_simple = simple_hash(self.name)
        self.hash_hard = hard_hash(self.name)


class HashTable:

    def __init__(self):
        self.key_simple = [None] * MAXSIZE
        self.value_simple = [[None]] * MAXSIZE
        self.key_hard = [None] * MAXSIZE
        self.value_hard = [[None]] * MAXSIZE
        self.collisions_simple = 0
        self.collisions_hard = 0

    def insert(self, prod):
        self.collisions_simple = self.add(prod.name, prod, prod.hash_simple, self.key_simple,
                                                        self.value_simple, self.collisions_simple)
        self.collisions_hard = self.add(prod.name, prod, prod.hash_hard, self.key_hard,
                                                       self.value_hard, self.collisions_hard)

    def add(self, key, value, _hash, array_key, array_value, collisions_count):
        if not array_key[_hash]:
            array_key[_hash] = key
            array_value[_hash] = [value]
        elif array_key[_hash] == key:
            array_value[_hash].append(value)
        else:
            collisions_count += 1
            new_hash = get_new_pos(_hash)
            while array_key[new_hash] and array_key[new_hash] != key:
                new_hash = get_new_pos(new_hash)

            if not (array_key[new_hash]):
                array_key[new_hash] = key
                array_value[new_hash] = [value]
            elif array_key[new_hash] == key:
                array_value[new_hash].append(value)
        return collisions_count

    def get(self, key, _hash, array_key, array_value):
        value = None
        new_hash = _hash
        while array_key[new_hash] and array_key[new_hash] != key:
            new_hash = get_new_pos(new_hash)
            if new_hash == _hash:
                break
        if array_key[new_hash] == key:
            value = array_value[new_hash]
        return value

    def find_simple(self, key):
        value = self.get(key, simple_hash(key), self.key_simple, self.value_simple)
        if not value:
            return 'Ключ не найден'
        else:
            return value[0]

    def find_hard(self, key):
        value = self.get(key, hard_hash(key), self.key_hard, self.value_hard)
        if not value:
            return 'Ключ не найден'
        else:
            return value[0]
