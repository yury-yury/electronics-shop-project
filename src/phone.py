from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self._number_of_sim = number_of_sim
        else:
            raise ValueError('The number of physical SIM cards must be an integer greater than zero.')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value > 0 and isinstance(value, int):
            self._number_of_sim = value
        else:
            raise ValueError('The number of physical SIM cards must be an integer greater than zero.')
