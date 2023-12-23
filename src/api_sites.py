import os
from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import requests
import json


class SitesAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями."""

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(SitesAPI):
    """Класс для работы с API hh.ru."""

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

    def get_vacancies(self) -> list:
        list_vacancies = []
        data = requests.get(f'{self.url}vacancies', params={'text': self.text, 'search_field': "name",
                                                            'area': self.get_code_region()}).json()

        for item in data['items']:
            if item["salary"]["from"] is not None and item["salary"]["to"] is not None:
                vacancy = Vacancy(
                    item["employer"]["name"],
                    item["name"],
                    item["address"]["raw"],
                    item["alternate_url"],
                    item["salary"]["from"],
                    item["salary"]["to"],
                    item["salary"]["currency"]
                )
                list_vacancies.append(vacancy)

        return list_vacancies

    @staticmethod
    def create_file_with_vacancies(list_vacancies):

        with open('HeadHunter_vacancies.json', 'a') as f:
            for vacancy in list_vacancies:
                json.dump(vacancy.get_dict_vacancy(), f)


class SuperJobAPI(SitesAPI):
    """Класс для работы с API superjob.ru."""

    def __init__(self, text, region_name):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.text = text
        self.region_name = region_name.lower()

    def get_vacancies(self) -> list:
        list_vacancies = []
        headers = {
            'X-Api-App-Id': os.getenv('JOB_API_KEY'),
        }
        data = requests.get(self.url, headers=headers, params={'keys': self.text, 'srws': 1, 'skwc': 'or',
                                                               'town': self.region_name}).json()

        for item in data['objects']:
            if item["payment_from"] is not None:
                vacancy = Vacancy(
                    item["firm_name"],
                    item["profession"],
                    item["address"],
                    item["link"],
                    item["payment_from"],
                    item["payment_to"],
                    item["currency"]
                )
                list_vacancies.append(vacancy)

        return list_vacancies

    @staticmethod
    def create_file_with_vacancies(list_vacancies):

        with open('SuperJob_vacancies.json', 'a') as f:
            for vacancy in list_vacancies:
                json.dump(vacancy.get_dict_vacancy(), f)
