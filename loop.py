
from job import JobAPI, HhAPI
from vacancy_file import VacancyFile

job = JobAPI(token='v3.r.137524326.7f1f58cab26a5c76edc518d930de363295365423.6828e6b57c815049d3942ab4781345a5fce09ed2')
print(vacs := job.search_vacancies(title=input()))

VacancyFile('vac.json').dump_vac(vacs)


job = HhAPI()
print(vacs := job.search_vacancies(title=input()))

VacancyFile('vac.json').dump_vac(vacs)
