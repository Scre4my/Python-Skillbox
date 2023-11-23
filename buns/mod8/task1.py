class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        pass

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        pass


class Passenger:
    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        pass

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        pass


class Cargo:
    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        pass


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass


class Seaplane(Plane, Ship):
    pass