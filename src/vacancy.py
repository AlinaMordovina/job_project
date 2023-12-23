"""Создать класс для работы с вакансиями.
В этом классе самостоятельно определить атрибуты, такие как название вакансии,
ссылка на вакансию, зарплата, краткое описание или требования и т. п. (не менее четырех).
Класс должен поддерживать методы сравнения вакансий между собой по зарплате
и валидировать данные, которыми инициализируются его атрибуты."""


class Vacancy:
    """Класс для работы с вакансией."""

    def __init__(self, company_name, name_vacancy, address, url_vacancy, salary_min, salary_currency,
                 salary_max='Не указано'):
        self.company_name = company_name
        self.name_vacancy = name_vacancy
        self.address = address
        self.url_vacancy = url_vacancy
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.salary_currency = salary_currency

    def __str__(self):
        return (f"Вакансия: {self.name_vacancy}\n"
                f"Зарплата: от {self.salary_min} до {self.salary_max}\n"
                f"Компания: {self.company_name}\n"
                f"Адрес: {self.address}\n"
                f"Подробнее о вакансии можно посмотреть по ссылке: {self.url_vacancy}\n\n")\


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

    def get_dict_vacancy(self):
        return {
            'company_name': self.company_name,
            'name_vacancy': self.name_vacancy,
            'address': self.address,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'salary_currency': self.salary_currency,
            'url_vacancy': self.url_vacancy
        }


class Vacancies:
    """Вспомогательный класс для обработки списка вакансий."""

