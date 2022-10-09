def matrixadd (mart1 , matr2) : 
    resmatr = []
    for i in range (len(matr1)) :
        row = []
        for j in range (len(matr1[0])) :
            row.append (matr1[i][j] + matr2[i][j])
        resmatr.append(row)
    return resmatr

def read_from_file (file) :
    matr = []
    for row in file :
       
        if len(row) == 1 :
            continue
        else :
            row = row.split ()
            for i in range (len(row)) :
                row[i]= int (row[i]) # робить з рядка число
            matr.append (row)  
    return matr

def save_to_file (file, matr) :
       for i in range (len(matr1)) :
        for j in range (len(matr1[0])) :
            file.write(str(matr[i][j])+' ')# перетворюємо рядок в ціле число 
        file.write ('\n')            

    
file1 = open("matr1.txt", "r")
file2 = open("matr2.txt", "r")
matr1 = read_from_file (file1)
matr2 = read_from_file (file2)
file1.close()
file2.close()

resfile = open("resmatr.txt", "w")
try :
    if len(matr1) == len(matr2) and len(matr1[0]) == len(matr2[0]) :
        matr = matrixadd (matr1,matr2)
        save_to_file (resfile, matr)
        resfile.close()
        for i in range (len(matr)) :
            for j in range (len(matr[0])) :
              print (matr[i][j], end = " ")
            print  ()
    else :
       raise Exception

    
except Exception:
    print('Matrices have  different sizes')
    exit()
     

