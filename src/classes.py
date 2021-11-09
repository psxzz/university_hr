# Base class for person classes
class Person(object):
    def __init__(self):
        pass


class Student(Person):
    def __init__(self):
        super().__init__()


class Teacher(Person):
    def __init__(self):
        super().__init__()

# Base class for structure classes 
class Structure(object):
    def __init__(self):
        pass


class Department(Structure):
    def __init__(self):
        super().__init__()


class Group(Structure):
    def __init__(self):
        super().__init__()
