#Задача "История строительства":
#Для решения этой задачи будем пользоваться решением к предыдущей задаче


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):  # ,*args, **kwargs
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name:str, number_of_floors:int):
        """Иницилизируем экзепляр по аттрибутам"""
        self.name = name
        self.number_of_floors = number_of_floors
        #self.houses_history.append(name)

    def __len__(self):
        """ Охарактеризум объект по количеству этажей"""
        return self.number_of_floors

    def __str__(self):
        """не строгое описание экземпляра"""
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self, new_floor:int):
        if 1 <= new_floor <= self.number_of_floors:
            go_to = [x for x in range(1, new_floor + 1)]
            print(*go_to)
        else:
            print(f"{new_floor} этажа не существует в доме {self.name!r}")

    def __eq__(self, other):
        """Методом сравнения на равенства: возвращаем True, если количество этажей self == other """
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')

        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        """Методом сравнения "меньше чем" (Lower than)"""
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')
        return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        """Методом сравнения "меньше или равно"""
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        """Методом сравнения "больше чем" (Greater than)"""

        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        """Методом сравнения "больше или равно"""
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        """Методом сравнения на неравенство"""
        if not isinstance(other, House):
            raise TypeError('Сравниваемые экземпляры не принадлежат к одному классу House')
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        """Методом добавления элемента в множество"""
        if not isinstance(value, int):
            raise ArithmeticError('Необходимо добавлять значения только из целых чисел')
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        """Методом симметричного сложения"""
        if not isinstance(value, int):
            raise ArithmeticError('Необходимо добавлять значения из целых чисел ')
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        """Методом сложения с присваиванием +="""
        if not isinstance(value, int):
            raise ArithmeticError('Необходимо добавлять значения из целых чисел ')
        self.number_of_floors += value
        return self

    def __del__(self):
        print(self.name, ' снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
# del h2
# del h3

print(House.houses_history)




