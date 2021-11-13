# Base class for person classes
class Person(object):
    def __init__(self, lastname, firstname, secondname, phone, department):
        self._last_name = lastname
        self._first_name = firstname
        self._second_name = secondname
        self._phone_number = phone
        self._department = department


class Student(Person):
    def __init__(
        self, lastname, firstname, secondname, phone, department, birthdate, gradebook
    ):
        super().__init__(lastname, firstname, secondname, phone, department)
        self._birth_date = birthdate
        self._gradebook_number = gradebook


class Teacher(Person):
    def __init__(self, id, lastname, firstname, secondname, phone, department):
        super().__init__(lastname, firstname, secondname, phone, department)
        self._id = id


# Base class for structure classes
class Structure(object):
    def __init__(self, id, fullname, shortname):
        self._id = id
        self._full_name = fullname
        self._short_name = shortname


class Department(Structure):
    def __init__(self, id, fullname, shortname, head):
        super().__init__(id, fullname, shortname)
        self._department_head = head


class Group(Structure):
    def __init__(self, id, fullname, shortname, students, department):
        super().__init__(id, fullname, shortname)
        self._students_count = students
        self._department = department
