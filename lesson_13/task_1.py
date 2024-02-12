class Person:
    __name = "no name"
    __age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name):
            if len(name) > 2:
                self.__name = name

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, age):
            if age > 18:
                self.__age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


katya = Person("Katya", 37)
katya.show_info()
print(katya.__dict__)


class Teacher(Person):
    def __init__(self, name, age, academy= None):
        super().__init__(name, age)
        self.academy = academy

    def work(self):
        print(f"{self.name} works in {self.academy} academy")

    def show_info(self):
        super().show_info()
        print(f"Academy: {self.academy}")


alex = Teacher("Alexey", 40, "Medical academy")
alex.show_info()
print(alex.__dict__)


class Student(Person):
    def __init__(self, name, age, university=None):
        super().__init__(name, age)
        self.university = university

    def study(self):
        print(f"{self.name} study at {self.university} university")

    def show_info(self):
        super().show_info()
        print(f"University: {self.university}")


peter = Student("Peter", 20, "Tech")
peter.show_info()
print(peter.__dict__)

