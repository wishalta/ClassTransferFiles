


class Discipline():
    def __init__(self, title = "", grades = []):
        self.Title = title
        self.Grades = grades

    def __str__(self):
        return f'{self.Title} {self.Grades}'