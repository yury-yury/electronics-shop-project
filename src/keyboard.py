from enum import Enum

from src.item import Item


class Language(Enum):
    EN = 'EN'
    RU = 'RU'

    def __str__(self):
        return self


class KeyBoard(Item):
    def __init__(self, name: str, price: float, quantity: int, language: Language = 'EN') -> None:
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language

    def change_lang(self) -> None:
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self
