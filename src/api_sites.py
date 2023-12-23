import os
from abc import ABC, abstractmethod
import requests
"""Создать абстрактный класс для работы с API сайтов с вакансиями.
Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами.
Классы должны уметь подключаться к API и получать вакансии."""


class SitesAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(SitesAPI):

    def __init__(self, text, region_name):
        self.url = "https://api.hh.ru/"
        self.text = text
        self.region_name = region_name.lower()

    def get_code_region(self):
        regions = requests.get(f'{self.url}areas/113').json()
        for region in regions['areas']:
            for city in region['areas']:
                if self.region_name in city['name'].lower():
                    return city['id']

    def get_vacancies(self):

        data = requests.get(f'{self.url}vacancies', params={'text': self.text, 'search_field': "name",
                                                            'area': self.get_code_region()}).json()
        print(data)


class SuperJobAPI(SitesAPI):

    def __init__(self, text, region_name):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.text = text
        self.region_name = region_name.lower()

    def get_vacancies(self):
        headers = {
            'X-Api-App-Id': os.getenv('JOB_API_KEY'),
        }
        data = requests.get(self.url, headers=headers, params={'keys': self.text, 'srws': 1, 'skwc': 'or',
                                                               'town': self.region_name}).json()
        print(data)
