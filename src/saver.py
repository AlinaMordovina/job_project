from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy
from operator import itemgetter


class Saver(ABC):
    """Абстрактный класс обработки списка вакансий."""

    @abstractmethod
    def add_vacancies_to_file(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies_from_file_by_salary(self, salary_min, salary_max):
        pass

    @abstractmethod
    def get_vacancies_from_file_sorted_by_salary(self):
        pass

    @abstractmethod
    def remove_info_about_vacancies_from_file(self):
        pass


class JsonSaver(Saver):
    """Класс для сохранения и обработки списка вакансий в JSON формате."""

    def __init__(self, site):
        self.file_name = f"{site}_vacancies.json"

    def add_vacancies_to_file(self, vacancies):
        list_vacancies = []
        for vacancy in vacancies:
            list_vacancies.append(vacancy.get_dict_vacancy())

        with open(self.file_name, 'w') as f:
            json.dump(list_vacancies, f, ensure_ascii=False, indent=2)

    def get_vacancies_from_file_by_salary(self, salary_min=0, salary_max=0):
        list_vacancies_with_salary = []

        with open(self.file_name, 'r') as f:
            list_vacancies = json.load(f)
        for vacancy in list_vacancies:
            if vacancy["salary_min"] >= salary_min and vacancy["salary_max"] <= salary_max:
                list_vacancies_with_salary.append(Vacancy.from_dict_to_example_vacancy(vacancy))

        if not list_vacancies_with_salary:
            return None
        else:
            return list_vacancies_with_salary

    def get_vacancies_from_file_sorted_by_salary(self):
        list_vacancies_with_sort = []

        with open(self.file_name, 'r') as f:
            list_vacancies = json.load(f)
        for vacancy in sorted(list_vacancies, key=itemgetter('salary_min', 'salary_max')):
            list_vacancies_with_sort.append(Vacancy.from_dict_to_example_vacancy(vacancy))

        return list_vacancies_with_sort

    def remove_info_about_vacancies_from_file(self):
        open(self.file_name, "w").close()
