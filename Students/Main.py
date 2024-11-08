import datetime

from Students.Discipline import Discipline
from Students.Student import Student
from Students.Study import Study

matematika = Discipline()
matematika.Title = "Matematika"
matematika.Grades = [10, 9, 7, 10, 9, 3, 5]

fizika = Discipline()
fizika.Title = "Fizika"
fizika.Grades = [8, 9, 7, 7, 9, 6, 5]

istorija = Discipline()
istorija.Title = "Istorija"
istorija.Grades = [9, 8, 7, 6, 4, 3, 5]

study = Study()
study.title = "Taikomoji fizika"
study.Disciplines = [matematika, fizika, istorija]

stud = Student()
stud.name = "Mick"
stud.surname = "Jordan"
stud.birth_date = datetime.date(1980, 9, 10)
stud.studies = study

study.Disciplines[0].Grades




