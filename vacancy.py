class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, title, url, salary, description):
        """
        Конструктор класса Vacancy.

        :param title: заголовок вакансии.
        :param url: ссылка на вакансию.
        :param salary: зарплата.
        :param description: описание вакансии.
        """
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
            'salary': self.salary,
            'description': self.description
        }

    def __str__(self):
        return f"{self.title} ({self.salary})"

    def __repr__(self):
        return f"{self.title} ({self.salary})\n"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary
