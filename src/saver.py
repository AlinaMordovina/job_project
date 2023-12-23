from abc import ABC, abstractmethod
import json
""""Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям и удаления информации о вакансиях.
Создать класс для сохранения информации о вакансиях в JSON-файл.
Дополнительно (по желанию) можно реализовать классы для работы с другими форматами,
например с CSV-, Excel- или TXT-файлом."""


class Saver(ABC):
    """Абстрактный класс обработки списка вакансий."""

    @abstractmethod
    def create_file_with_vacancies(self, list_vacancies, site):
        pass

    @abstractmethod
    def add_vacancy_to_file(self):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass

    @abstractmethod
    def remove_info_about_vacancy(self):
        pass


class JSONSaver(Saver):
    """Класс для сохранения и обработки списка вакансий в JSON формате."""

    def create_file_with_vacancies(self, list_vacancies, site):
        file = f'{site}_vacancies.json'

        with open(file, 'a', encoding='utf-8') as f:
            for vacancy in list_vacancies:
                json.dump(vacancy.get_dict_vacancy(), f)

    def add_vacancies_to_file(self):
        pass

    def get_data_from_file(self):
        pass

    def remove_info_about_vacancy(self):
        pass
