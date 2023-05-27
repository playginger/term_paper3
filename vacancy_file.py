import json
from abc import ABC
from googletrans import Translator
from vacancy import Vacancy


class VacancyFile(ABC):
    """Абстрактный класс для работы с файлом вакансий."""

    def __init__(self, filename):
        self.filename = filename

    def dump_vac(self, vacs):
        with open(self.filename, 'a', encoding='utf-8') as f:
            vacs = [vac.to_dict() for vac in vacs]
            json.dump(vacs, f, ensure_ascii=False)
            f.write('\n')  # добавляем перевод строки между вакансиями


class JsonVacancyFile(VacancyFile):
    """Класс для работы с JSON-файлом вакансий."""

    def __init__(self, filename):
        super().__init__(filename)

    def add_vacancy(self, vacancy):
        with open(self.filename, 'a', encoding='utf-8') as f:
            vacancy_dict = vacancy.to_dict()
            translator = Translator()
            for key, value in list(vacancy_dict.items()):
                value_ru = translator.translate(str(value), src='en', dest='ru').text
                vacancy_dict[f'{key}_ru'] = value_ru
            json.dump(vacancy_dict, f, ensure_ascii=False)
            f.write('\n')  # добавляем перевод строки для следующей вакансии

    def get_vacancies(self, **kwargs):
        vacancies = []
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                vacancies.append(Vacancy(**data))
        return vacancies

    def delete_vacancy(self, vacancy):
        with open(self.filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        with open(self.filename, 'w', encoding='utf-8') as f:
            for line in lines:
                data = json.loads(line)
                if data != vacancy.to_dict():
                    json.dump(data, f, ensure_ascii=False)
                    f.write('\n')
