

class Plant():
    def __init__(self, name="", latin_name="", is_annual=False, continent="", height=0, eatable=False):
        self.Name = name
        self.Latin_name = latin_name
        self.Is_annual = is_annual
        self.Continent = continent
        self.Height = height
        self.Eatable = eatable
    def __str__(self):
        return f'Name: {self.Name} | Latin_name: {self.Latin_name} | Annual: {self.Is_annual} | Continent: {self.Continent} | Max high: {self.Height}m. | Eatable: {self.Eatable}'