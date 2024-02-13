class Academy:
    def __init__(self, name, number_of_departments):
        self.__name = name
        self.__number_of_departments = number_of_departments

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_of_academy):
        if len(name_of_academy) > 2:
            self.__name = name_of_academy
        else:
            raise ValueError("Name should be at least 3 characters long")

    @property
    def number_of_departments(self):
        return self.__number_of_departments

    @number_of_departments.setter
    def number_of_departments(self, departments):
        if departments > 2:
            self.__number_of_departments = departments
        else:
            raise ValueError("Number of departments should be greater than 2")

    def show_info(self):
        print(f"The {self.__name} academy has {self.__number_of_departments} departments")


class Department(Academy):
    def __init__(self, name, number_of_departments, name_of_department=None):
        super().__init__(name, number_of_departments)
        self.name_of_department = name_of_department

    @property
    def name_of_department(self):
        return self.__name_of_department

    @name_of_department.setter
    def name_of_department(self, name_dep):
        if len(name_dep) > 2:
            self.__name_of_department = name_dep
        else:
            raise ValueError("Name of department should be at least 3 characters long")

    def department(self):
        print(f"The name of department is {self.__name_of_department}.")

    def show_info(self):
        super().show_info()
        print(f"Department: {self.__name_of_department}")


medic = Department("Medical", 3, "Anatomic")
medic.show_info()
