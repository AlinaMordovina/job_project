from abc import ABC, abstractmethod
from src.api_sites import HeadHunterAPI, SuperJobAPI
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

    def __init__(self, name, url, salary, short_description):
        self.name = name
        self.url = url
        self.salary = salary
        self.short_description = short_description


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
