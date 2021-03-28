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

    def __gt__(self, other):  # перегрузка  '>'
        if self.name > other.name:
            return True
        elif self.name == other.name:
            if self.volume > other.volume:
                return True
            elif self.volume == other.volume:
                if self.country > other.country:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __lt__(self, other):  # перегрузка '<'
        if self.name < other.name:
            return True
        elif self.name == other.name:
            if self.volume < other.volume:
                return True
            elif self.volume == other.volume:
                if self.country < other.country:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, other):  # перегрузка '>='
        if self.name > other.name:
            return True
        elif self.name == other.name:
            if self.volume > other.volume:
                return True
            elif self.volume == other.volume:
                if self.country > other.country:
                    return True
                elif self.country == other.country:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, other):  # перегрузка '<='
        if self.name < other.name:
            return True
        elif self.name == other.name:
            if self.volume < other.volume:
                return True
            elif self.volume == other.volume:
                if self.country < other.country:
                    return True
                elif self.country == other.country:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
