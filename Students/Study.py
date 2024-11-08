


class Study():
    def __init__(self, title = "", disciplines = []):
        self.Title = title
        self.Disciplines = disciplines
        self.Disciplines = self.listToDict(disciplines)
    # def __str__(self):
    #     return f'{self.Title} {self.Discipline}'

    def listToDict(self):
        dict = {}
        for dis in self.Disciplines:
            print(dis)
        return dict