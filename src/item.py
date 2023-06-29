from csv import DictReader
from enum import Enum


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_name = '../src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.__name}'

    def __add__(self, other) -> int:
        if not isinstance(other, Item):
            raise ValueError('You can only add Item objects and their children.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name_: str) -> None:
        if len(name_) <= 10:
            self.__name = name_
        else:
            raise Exception('The length of the name attribute must be less than or equal to 10 characters.')

    @classmethod
    def instantiate_from_csv(cls) -> None:
        try:
            with open(f'{cls.file_name}', 'r', encoding='windows-1251') as file:
                file_dict = DictReader(file)
                for row in file_dict:
                    Item(name=row['name'], price=row['price'], quantity=row['quantity'])
        except FileNotFoundError:
            print('The item.csv file is missing')
            raise FileNotFoundError(f'The {cls.file_name} file is missing')
        except Exception:
            raise InstantiateCSVError


    @staticmethod
    def string_to_number(value: str) -> int:
        try:
            result = int(float(value))
        except Exception:
            raise Exception('The passed string must consist of digits.')
        else:
            return result


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Incorrect data is received or the file is corrupted.'

    def __str__(self):
        return self.message
