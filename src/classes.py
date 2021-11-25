# Base class for person classes
class Person(object):
    def __init__(self, lastname, firstname, secondname, phone, structure):
        self._last_name = lastname
        self._first_name = firstname
        self._second_name = secondname
        self._phone_number = phone
        self._structure_name = structure


    def show(self):
        print(f"ФИО: {self._second_name} {self._first_name} {self._last_name}")
        print(f"Телефон: {self._phone_number}")


class Student(Person):
    def __init__(
        self, gradebook, firstname, secondname, lastname, phone, birthdate, department 
    ):
        super().__init__(lastname, firstname, secondname, phone, department)
        self._birth_date = birthdate.strftime('%d.%m.%Y')
        self._gradebook_number = gradebook
    

    def show(self):
        print(f"Студент: {self._gradebook_number}")
        print(f"Кафедра: {self._structure_name}")
        super().show()
        print(f"Дата рождения: {self._birth_date}")


class Teacher(Person):
    def __init__(self, id, firstname, secondname, lastname, phone, institute):
        super().__init__(lastname, firstname, secondname, phone, institute)
        self._id = id


    def show(self):
        print(f"Преподаватель: {self._id}")
        print(f"Институт: {self._structure_name}")
        super().show()


# Base class for structure classes
class Structure(object):
    def __init__(self, id, fullname, shortname):
        self._id = id
        self._full_name = fullname
        self._short_name = shortname


class Institute(Structure):
    def __init__(self, id, fullname, shortname, head):
        super().__init__(id, fullname, shortname)
        self._department_head = head

    
    def show(self):
        print(f"Институт: {self._id}")
        print(f"Полное название: {self._full_name}")
        print(f"Сокращенное название: {self._short_name}")
        print(f"ID директора института: {self._department_head}")


class Department(Structure):
    def __init__(self, id, fullname, shortname, students, institute):
        super().__init__(id, fullname, shortname)
        self._students_count = students
        self._structure_name = institute

    
    def show(self):
        print(f"Группа: {self._id}")
        print(f"Институт: {self._structure_name}")
        print(f"Полное название: {self._full_name}")
        print(f"Сокращенное название: {self._short_name}")
        print(f"Количество студентов на кафедре: {self._students_count}")
