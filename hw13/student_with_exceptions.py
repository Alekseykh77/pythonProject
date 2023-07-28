import csv
from functools import reduce
from pathlib import Path
from user_exceptions import *


class Validate:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, str):
            raise UserTypeStrError(value)
        if not value.isalpha() or not value.istitle():
            raise UserTypeTextError(value)


class Student:
    name = Validate()
    second_name = Validate()
    surname = Validate()
    _subjects = None

    def __init__(self, name: str, second_name: str, surname: str, subjects: Path):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.subjects = subjects

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, sub: Path):
        if self.subjects is not None:
            raise AttributeError(f'Список предметов уже определён')
        self._subjects = {"subjects": {}}
        with open(sub, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._subjects["subjects"][row[0]] = {"estimates": [],
                                                      "tests": [],
                                                      "middle_estimate_test": None}
        self._subjects["middle_estimate"] = None

    def new_estimate(self, name_of_subject: str, number: int, type_est: str = "sub"):
        if name_of_subject not in self.subjects["subjects"].keys():
            raise UserSubjectsError(name_of_subject)
        if type_est == "sub":
            if number < 2 or number > 5:
                raise UserEstimateError(number, 2, 5)
            self.subjects["subjects"][name_of_subject]["estimates"].append(number)
            self.subjects["middle_estimate"] = self.middle_estimate(self.subjects)
        elif type_est == "test":
            if number < 0 or number > 100:
                raise UserEstimateError(number, 0, 100)
            self.subjects["subjects"][name_of_subject]["tests"].append(number)
            self.subjects["subjects"][name_of_subject]["middle_estimate_test"] = \
                reduce(lambda x, y: x + y, self.subjects["subjects"][name_of_subject]["tests"]) / \
                len(self.subjects["subjects"][name_of_subject]["tests"])

    @staticmethod
    def middle_estimate(subjects: dict):
        all_estimates = []
        [all_estimates.extend(subjects["subjects"][name]["estimates"]) for name in subjects["subjects"]]
        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    def __repr__(self):
        result = f'''Student
full_name = "{self.name} {self.second_name} {self.surname}"
middle_estimate = {self.subjects["middle_estimate"]}\n'''
        for key, value in self.subjects["subjects"].items():
            result += f'{key} = {value["middle_estimate_test"]}\n'

        return result


if __name__ == '__main__':
    mik = Student("Ivan", "Ivanovich", "Ivanov", Path('subjects.csv'))
    print(mik)
    mik.new_estimate("русский язык", 5)
    mik.new_estimate("химия", 5)
    mik.new_estimate("физика", 4)
    mik.new_estimate("физика", 4)
    mik.new_estimate("математика", 5)
    mik.new_estimate("русский язык", 4)
    mik.new_estimate("химия", 4)
    mik.new_estimate("физика", 5)
    mik.new_estimate("физика", 4)
    mik.new_estimate("математика", 4)
    mik.new_estimate("математика", 82, "test")
    mik.new_estimate("математика", 88, "test")
    mik.new_estimate("физика", 77, "test")
    mik.new_estimate("физика", 81, "test")
    mik.new_estimate("русский язык", 72, "test")
    mik.new_estimate("русский язык", 87, "test")
    mik.new_estimate("история", 73, "test")
    mik.new_estimate("история", 74, "test")
    mik.new_estimate("химия", 75, "test")
    mik.new_estimate("химия", 89, "test")
    print(mik)
