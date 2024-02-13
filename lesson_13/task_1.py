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


class Teacher(Person):
    __academy = "no name"

    def __init__(self, name, age, academy=None):
        super().__init__(name, age)
        self.academy = academy

    def work(self):
        print(f"{self.name} works in {self.academy} academy")

    def show_info(self):
        super().show_info()
        print(f"Academy: {self.academy}")


class Student(Person):
    __university = "no name"

    def __init__(self, name, age, university=None):
        super().__init__(name, age)
        self.university = university

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, name_univer):
        if len(name_univer) > 3:
            self.__university = name_univer

    def study(self):
        print(f"{self.name} study at {self.university} university")

    def show_info(self):
        super().show_info()
        print(f"University: {self.university}")


test = Student("Peter", 30, "Agriculture")
test.show_info()


class Head_teacher(Teacher):
    __subject = "no name"
    def __init__(self, name, age, academy, subject=None):
        super().__init__(name, age, academy)
        self.__subject = subject
    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self,name_subject):
        if len(name_subject) > 4:
            self.__subject = name_subject

    def show_info(self):
        print(f"The head teacher of {self.academy} academy is {self.name}, age {self.age}. The subject is {self.__subject}")


test = Head_teacher("Peter", 35, "Technical", "Math")
test.show_info()
print(test.__dict__)
print(Head_teacher.mro())
