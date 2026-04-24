class Student:
    def __init__(self, full_name, group_number, birth_date, address=""):
        self.full_name = full_name
        self.group_number = group_number
        self.birth_date = birth_date
        self.address = address

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        if not value.strip():
            raise ValueError("Full name cannot be empty.")
        self.__full_name = value.strip()

    @property
    def group_number(self):
        return self.__group_number

    @group_number.setter
    def group_number(self, value):
        if not value.strip():
            raise ValueError("Group number cannot be empty.")
        self.__group_number = value.strip()

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        if not value.strip():
            raise ValueError("Birth date cannot be empty.")
        self.__birth_date = value.strip()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value.strip()
