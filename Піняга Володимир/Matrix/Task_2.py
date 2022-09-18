class differSize( Exception ): #клас для ексшепшину

    pass


def Enter_Matrix(fileName): #ввід матриць з файлу
    with open(fileName, 'r') as file:
        matrix = [[int(element) for element in matrix_str.split(' ')] for matrix_str in file]

    return matrix


def Add_2matrix(mat1, mat2, fileName): #дод. 2 матриць
    if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        file = open(fileName, 'a')
        file.write(str(differSize("Matrixes don`t have same size!"))+'\n')

        raise differSize("Matrixes don`t have same size!")

    else:
        res_matrix = []

        for iter in range(len(mat1)):
            row = []
            for jter in range(len(mat1[0])):
                row.append(0)
            res_matrix.append(row)

    for iter in range(len(mat1)):
        for jter in range(len(mat1[0])):
            res_matrix[iter][jter] = mat1[iter][jter] + mat2[iter][jter]

    return res_matrix


def write(Matrix, fileName): #запис у файл результату
    file = open(fileName, 'a')

    for iter in Matrix:
        file.write(str(iter)+'\n')


#ексепшн
try:
    mat1 = Enter_Matrix('text1.txt')
    mat2 = Enter_Matrix('text2.txt')
    result_matrix = Add_2matrix(mat1, mat2, 'text3.txt')

    write(result_matrix, 'text3.txt')

except differSize as error:
    print(error)