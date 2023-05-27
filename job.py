from abc import ABC

import requests

from vacancy import Vacancy


class JobAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    def __init__(self, token=None):
        self.headers = {
            'X-Api-App-Id': 'v3.r.137524326.7f1f58cab26a5c76edc518d930de363295365423'
                            '.6828e6b57c815049d3942ab4781345a5fce09ed2'
        }

    def search_vacancies(self, title='python', count=10):
        """
        Метод для поиска вакансий на сайте.
        :param count:
        :param title: строка запроса для поиска вакансий.
        :return: список вакансий в виде объектов-экземпляров класса Vacancy.
        """
        params = {
            'keywords': title,
            'not_archive': 1,
            'count': count,
            'page': 0
        }

        result = requests.get("https://api.superjob.ru/2.0/vacancies/", params, headers=self.headers)
        result = result.json()

        vacs = []
        for vac in result['objects']:
            vacs.append(Vacancy(title=vac['profession'], url=vac['link'], salary=vac['payment_from'],
                                description=vac['vacancyRichText']))

        return vacs


class HhAPI(ABC):

    def __init__(self):
        pass

    def search_vacancies(self, title='python', count=90):
        params = {
            'text': title,
            'area': 113,
            'per_page': count,
            'only_with_salary': True,
            'search_field': 'name',
            'page': 0,
        }

        result = requests.get("https://api.hh.ru/vacancies", params, headers=None)
        result = result.json()

        vacs = []
        for vac in result['items']:
            vacs.append(Vacancy(title=vac['name'], url=vac['url'], salary=vac['salary']['from'],
                                description=vac['snippet']['requirement'] + vac['snippet']['responsibility']))

            return vacs
