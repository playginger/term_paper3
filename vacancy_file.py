import json
from abc import ABC, abstractmethod

from vacancy import Vacancy


class VacancyFile(ABC):
    """
    Абстрактный класс для работы с файлом вакансий.
    """

    def __init__(self, filename):
        self.filename = filename

    # @abstractmethod
    # def add_vacancy(self, vacancy):
    #     """
    #     Метод для добавления вакансии в файл.
    #     :param vacancy: объект-экземпляр класса Vacancy.
    #     """
    #     pass
    #
    # @abstractmethod
    # def get_vacancies(self, **kwargs):
    #     """
    #     Метод для получения списка вакансий из файла.
    #     :param kwargs: критерии поиска вакансий.
    #     :return: список вакансий в виде объектов-экземпляров класса Vacancy.
    #     """
    #     pass
    #
    # @abstractmethod
    # def delete_vacancy(self, vacancy):
    #     """
    #     Метод для удаления вакансии из файла.
    #     :param vacancy: объект-экземпляр класса Vacancy.
    #     """
    #     pass

    def dump_vac(self, vacs):
        with open('vac.json', 'w') as f:
            vacs = [vac.to_dict() for vac in vacs]

            json.dump(vacs, f)

# class JsonVacancyFile(VacancyFile):
#    """
#    Класс для работы с JSON-файлом вакансий.
#    """
#
#    def __init__(self, filename):
#        super().__init__(filename)
#
#    def add_vacancy(self, vacancy):
#        with open(self.filename, "a", encoding="utf-8") as f:
#            json.dump(vacancy.__dict__, f, ensure_ascii=False)
#
#    def get_vacancies(self, **kwargs):
#        vacancies = []
#        with open(self.filename, "r", encoding="utf-8") as f:
#            for line in f.readlines():
#                data = json.loads(line)
#                vacancies.append(Vacancy(**data))
#        return vacancies
#
#    def delete_vacancy(self, vacancy):
#        with open(self.filename, "r+", encoding="utf-8") as f:
#            lines = f.readlines()
#            f.seek(0)
#            for line in lines:
#                data = json.loads(line)
#                if data != vacancy.__dict__:
#                    f.write(line)
#            f.truncate()
#
#    def dump_vac(self, vacs):
#        with open('vac.json', 'w') as f:
#            vacs = [vac.to_dict() for vac in vacs]
#
#            json.dump(vacs, f)
#
