from classStudent import *
from datetime import date

def read_from_file(grupa):
       file = open("data.txt",'r')
       try:
            for line in file :
                if not line.isspace():
                    line = line.split(" ")
                    if len(line) == 4:
                        marks = []
                        for mark in line[3].split(","):
                            marks.append(int(mark))
                        data_birth = line[2].split(".")
                        year = int(data_birth[2])
                        month = int(data_birth[1])
                        day = int(data_birth[0])
                        student = Student(line[0], line[1], date(year, month, day), marks, 0)
                        student.average_mark()
                        grupa.append(student)
       except ValueError:
           print("wrong element type")

def print_rating(grupa):
    grupa.sort(key=lambda student: student.average)
    grupa = grupa[::-1]#в зворотньому порядку
    for st in grupa:
        st.student_print()
        


grupa = []
read_from_file(grupa)
print("Grupa:")
for st in grupa:
    st.student_print()
print("Dviyochnuku:")
Dviyochnuku = [student for student in grupa if 2 in student.marks]
for st in Dviyochnuku:
    st.Dviyochnuku_print()
print("\n Rating grupa :")
print_rating(grupa)



    






                    
                    
    
