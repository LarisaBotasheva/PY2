# TODO Написать 3 класса с документацией и аннотацией типов
class MultiCooker:
    def __init__(self, settings_amount: int, volume: float, height: int):
        if not isinstance(settings_amount, int):
            raise TypeError("Колличество режимов должно быть типа int")
        self.settings_amount = settings_amount
        if volume < 0:
            raise ValueError("Объем мультиварки не может быть меньше 0 литров")
        self.volume = volume
        if not isinstance(height, int):
            raise TypeError("Высота мультиварки должна быть типа int")
        self.volume = volume

class Toy:
    def __init__(self, colour: str, mass: float):
        if not isinstance(colour, str):
            raise TypeError("Цвет игрушки может быть только типа str")
        self.colour = colour
        if mass < 0:
            raise ValueError("Игрушка не может весить меньше 0 кг")
        self.mass = mass

class Towel:
    def __init__(self, colour_towel: str, length: int, width: int):
        if not isinstance(colour_towel, str):
            raise TypeError("Лучше записать не код цвета, а название цвета типом str")
        self.colour_towel = colour_towel
        if length < 0:
            raise ValueError("У полотенца длина больше 0 см")
        self.length = length
        if not isinstance(width, int):
            raise TypeError("Ширину полотенца лучше указать через int")
        self.width =  width

if __name__ == "__main__":
    Redmond = MultiCooker(7, 4.5, 25)
    Bosch = MultiCooker(10, 5.2, 28)
    Minion = Toy("желтый", 0.15)
    Owl = Toy("коричневый", 0.2)
    Face = Towel('серый', 40, 20)
    Body = Towel('синий', 120, 60)
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
