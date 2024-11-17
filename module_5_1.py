class House:  # зададим класс House
    # определим метод __init__ с названием и кол-вом этажей
    def __init__(self, name, number_of_floors):
        # присвоим атрибутам названия и кол-ва этажей атрибуты
        self.name = name
        self.number_of_floors = number_of_floors
        # выведем на экран ин-цию о моем доме
        print(f"Мой дом: {self.name} имеет {self.number_of_floors} этажей.")

    # зададим еще один метод - go_to с параметром номера эт. куда приедет лифт
    def go_to(self):
        # добавила возможность задать номер этажа - на экран выведется последовательность эт до нужного вкл.
        new_floor = int(input("Введите номер этажа: "))
        # если new_floor ниже первого этажа или больше кол-ва эт в доме, то вывод строки
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        # с помощью цикла for и ф-и range переберем возможные варианты от 1 до 30 включительно
        else:
            for floor in range (1, new_floor + 1):
                print(floor)

# зададим объект класса House
# home = House('ЖК Эльбрус', 30)
home = House('ЖК Лазурные небеса', 37)
home.go_to()
