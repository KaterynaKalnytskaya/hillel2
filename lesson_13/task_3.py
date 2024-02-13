class Department:
    def __init__(self, name_of_department, head_of_department):
        self.__name_of_department = "no name"
        self.__head_of_department = "no name"
        self.name_of_department = name_of_department
        self.head_of_department = head_of_department

    @property
    def name_of_department(self):
        return self.__name_of_department

    @name_of_department.setter
    def name_of_department(self, name_dep):
        if len(name_dep) > 2:
            self.__name_of_department = name_dep

    @property
    def head_of_department(self):
        return self.__head_of_department

    @head_of_department.setter
    def head_of_department(self, head_name):
        if len(head_name) > 4:
            self.__head_of_department = head_name

    def show_info(self):
        print(f"{self.head_of_department} is the head of department {self.name_of_department}.")


class Subject(Department):
    def __init__(self, name_of_department, head_of_department, name_subject=None):
        super().__init__(name_of_department, head_of_department)
        self.__name_subject = None
        self.name_subject = name_subject

    @property
    def name_subject(self):
        return self.__name_subject

    @name_subject.setter
    def name_subject(self, subject):
        if subject and len(subject) > 3:
            self.__name_subject = subject
        else:
            raise ValueError("Name of subject should be at least 4 characters long")

    def subject(self):
        print(f"Subject: {self.name_subject}")

    def show_info(self):
        super().show_info()
        print(f"Subject: {self.name_subject}")


test = Subject("Anatomy", "Tatyana Ivanova", "Path Anatomy")
test.show_info()
