from ClassBirthday import Birthday


class Student:
    def __init__(self, name: str, last_name: str, birth_date: Birthday, grades: list):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades
