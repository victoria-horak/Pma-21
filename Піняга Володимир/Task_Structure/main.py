from functions import *


Students = read_from_file("data.txt")
print("NAME    LAST_NAME   BIRTHDAY    GRADES")
print_info(Students)

print("===========Students who have a grade '2'==========")

sorted_Students = sorted(Students, key=sort_list)
students_with_grade2(sorted_Students)
