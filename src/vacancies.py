from abc import ABC, abstractmethod
"""Создать класс для работы с вакансиями.
В этом классе самостоятельно определить атрибуты, такие как название вакансии,
ссылка на вакансию, зарплата, краткое описание или требования и т. п. (не менее четырех).
Класс должен поддерживать методы сравнения вакансий между собой по зарплате
и валидировать данные, которыми инициализируются его атрибуты."""
"""Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям и удаления информации о вакансиях.
Создать класс для сохранения информации о вакансиях в JSON-файл.
Дополнительно (по желанию) можно реализовать классы для работы с другими форматами,
например с CSV-, Excel- или TXT-файлом."""


class Vacancy:

    def __init__(self, company_name, name_vacancy, address, url_vacancy, salary_min, salary_max, salary_currency):
        self.company_name = company_name
        self.name_vacancy = name_vacancy
        self.address = address
        self.url_vacancy = url_vacancy
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.salary_currency = salary_currency

    def __str__(self):
        return f'Вакансия располагается по адресу: {self.url_vacancy}'

    def __eq__(self, other):
        return self.salary_min == other.salary_min

    def __ne__(self, other):
        return self.salary_min != other.salary_min

    def __lt__(self, other):
        return self.salary_min < other.salary_min

    def __le__(self, other):
        return self.salary_min <= other.salary_min

    def __gt__(self, other):
        return self.salary_min > other.salary_min


class ControlVacancies(ABC):

    @abstractmethod
    def add_vacancy_to_file(self):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass

    @abstractmethod
    def remove_info_about_vacancy(self):
        pass
