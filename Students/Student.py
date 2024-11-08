import datetime

class Student():
    def __init__(self, name = "", surname = "", birth_date = datetime.date.today(), studies = []):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.studies = studies

    # def __str__(self):
    #     return f'{self.name} {self.surname} {self.birth_date} \n {self.studies}'

'''
Sukurti klasę Student
vardas (suformatuojame iki teisingo užrašymo)
pavardė (suformatuojame iki teisingo užrašymo)
gimimo data date
studies dictionary{
           "subject": pvz ekoligija
           "disciplines:[
                {"matematika": [8,7,9]},
                { "geografija": [7,5,6,10,8,9,9]}
            ]

sukurti metodą get_age() kuris gražintų tikslų, gražiai suformatuotą amžių su metais, mėnesiais ir dienomis
sukurti metodą, kuris padavus disciplinos pavadinimą gražintų jos pažymių vidurkį
sukurti metodą, kuris paskaičiuotų visų disciplinų(int) vidurkių vidurkį(double). galima kurtis pagalbines funkcijas.
parašyti __str__ kuris gražiai atspausdintų visą išsamią, gražiai suformatuotą studento informaciją

Vėliau studentą išskaidysime į kelias klases.
'''