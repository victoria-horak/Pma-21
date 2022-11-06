from Strucure_students import Student

def read_from_file(file_name):
    surname=" "
    name=" "
    date_of_birth=""
    points=0
    all_students=[]

    with open(file_name,"r") as file:
        for i in file:
            list_of_students=i.strip().split(" ")
            if list_of_students!=[""]:
                surname=list_of_students[0]
                name=list_of_students[1]
                date_of_birth=list_of_students[2]
                points=list_of_students[3].split(";")
                all_students.append(Student(surname,name,date_of_birth,points))
    
    return all_students

def point_two(all_students):
    point_two=[]
    for i in all_students:
        if "2" in i.points:
            point_two.append(i)
    if len(point_two)!=0:
        for i in range(0,len(point_two)):
            for j in range(0,len(point_two)-i-1):
                if point_two[j].surname>point_two[j+1].surname:
                    a=point_two[j]
                    point_two[j]=point_two[j+1]
                    point_two[j+1]=a
        return point_two
    else:
        print("No one has point to in this list!")


all_students=read_from_file("Students.txt")
point=point_two(all_students)
print("--STUDENTS WHO HAS 2:")
for i in point:
    print(i)