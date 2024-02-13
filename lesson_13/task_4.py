class Transport:
    __name = "no name"
    __year = 0

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_transport):
        if len(name_transport) > 2:
            self.__name = name_transport

    def show_info(self):
        print(f"Name: {self.name}\nYear: {self.year}")


class BaseAuto(Transport):
    __wheels_count = 0

    def __init__(self, name, year, wheels_count=0):
        super().__init__(name, year)
        self.__wheels_count = wheels_count

    @property
    def wheels_count(self):
        return self.__wheels_count

    @wheels_count.setter
    def wheels_count(self, wheels):
        if wheels > 1:
            self.__wheels_count = wheels

    def show_info(self):
        print(f"Wheels count: {self.wheels_count}")


class WaterTransport(Transport):
    __displacement = 0

    def __init__(self, name, year, displacement=0.):
        super().__init__(name, year)
        self.__displacement = displacement

    @property
    def displacement(self):
        return self.__displacement

    @displacement.setter
    def displacement(self, disp):
        if disp > 150:
            self.__displacement = disp

    def show_info(self):
        print(f"Displacement: {self.displacement}")


class Car(BaseAuto):
    __doors_count = 0

    def __init__(self, name, year, wheels_count, doors_count=0):
        super().__init__(name, year, wheels_count)
        self.__doors_count = doors_count

    @property
    def doors_count(self):
        return self.__doors_count

    @doors_count.setter
    def doors_count(self, doors):
        if doors > 1:
            self.__doors_count = doors

    def show_info(self):
        print(f"Doors count: {self.doors_count}")


class Amphibian(WaterTransport, BaseAuto):
    def __init__(self, name, year, wheels_count, displacement):
        WaterTransport.__init__(self, name, year, displacement)
        BaseAuto.__init__(self, name, year, wheels_count)

    def show_info(self):
        Transport.show_info(self)
        WaterTransport.show_info(self)
        BaseAuto.show_info(self)


test_car = Amphibian("BMW", 2024, 4, 123.2)
test_car.show_info()
print(Amphibian.mro())
