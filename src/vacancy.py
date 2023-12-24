class Vacancy:
    """Класс для работы с вакансией."""

    def __init__(self, company_name, name_vacancy, address, url_vacancy, salary_min, salary_max, salary_currency):
        self.company_name = company_name
        self.name_vacancy = name_vacancy
        self.address = address
        self.url_vacancy = url_vacancy
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.salary_currency = salary_currency

    def __str__(self):
        return (f"Вакансия: {self.name_vacancy}\n"
                f"Зарплата: от {self.salary_min} до {self.salary_max} {self.salary_currency}\n"
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
            'salary_min': int(self.salary_min),
            'salary_max': int(self.salary_max),
            'salary_currency': self.salary_currency,
            'url_vacancy': self.url_vacancy
        }

    @staticmethod
    def from_dict_to_example_vacancy(item):
        return Vacancy(
                    item["company_name"],
                    item["name_vacancy"],
                    item["address"],
                    item["url_vacancy"],
                    item["salary_min"],
                    item["salary_max"],
                    item["salary_currency"]
                    )
