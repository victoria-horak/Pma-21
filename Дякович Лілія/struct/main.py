from Struct import Student
from Functions import *

mass = read("data.txt")
for i in range(len(mass)):
    print(mass[i])
print("\n")
new_mass = grade2(mass)
new_mass = sorted(new_mass, key=lambda student: student.first_name)
for i in range(len(new_mass)):
    print(new_mass[i])
