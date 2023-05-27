from pprint import pprint

import requests as requests

params = {
    'keywords': 'python',
    'not_archive': 1,
    'count': 50,
    'page': 0
}

headers = {
    'X-Api-App-Id': 'v3.r.137524326.7f1f58cab26a5c76edc518d930de363295365423.6828e6b57c815049d3942ab4781345a5fce09ed2'
}

result = requests.get("https://api.superjob.ru/2.0/vacancies/", params, headers=headers)
result = result.json()
pprint(result)

params = {
    'text': 'python',
    'area': 113,
    'per_page': 100,
    'only_with_salary': True,
    'search_field': 'name',
    'page': 0,
}

result = requests.get("https://api.hh.ru/vacancies", params, headers=None)
result = result.json()
pprint(result)


