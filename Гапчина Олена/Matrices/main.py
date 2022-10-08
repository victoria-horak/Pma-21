class WrongSize(Exception):
    """The size of two matrices is not the same"""


def read_matrix_from_file(name_of_file):
    matrix = []
    f = open(name_of_file, 'r')
    read = f.read()
    f.close()
    split_read = read.split("\n")
    for row_iterator in range(0, split_read.__len__()):
        row_element = split_read[row_iterator]
        if row_element == '':
            continue
        column_elements = row_element.split(",")
        row = []
        for column_iterator in range(0, column_elements.__len__()):
            element = column_elements[column_iterator]
            if element == '':
                continue
            row.append(int(element))
        matrix.append(row)
    return matrix


# function for adding two matrices
def add_two_matrices(mtrx1, mtrx2):
    # len(mtrx1) - rows, len(mtrx1[0]) - columns
    if len(mtrx1) != len(mtrx2) or len(mtrx1[0]) != len(mtrx2[0]):
        raise WrongSize("The matrices have different size")
    # create a result matrix of the same size as to matrices to be added,
    # all elements of it are equal to 0
    result = [[0] * len(mtrx1[i]) for i in range(len(mtrx1))]
    # change "0"s to elements of the new matrix (sum)
    for i in range(len(mtrx1)):
        for j in range(len(mtrx1[i])):
            result[i][j] = mtrx1[i][j] + mtrx2[i][j]
    return result


def print_matrix(name_of_matrix):
    for row_iterator in range(len(name_of_matrix)):
        print(str(name_of_matrix[row_iterator]))


def write_matrix_into_file(name_of_matrix, name_of_file):
    f = open(name_of_file, 'w')
    for row_iterator in range(len(name_of_matrix)):
        f.write(str(name_of_matrix[row_iterator]) + '\n')
    f.close()


print("First Matrix:")
first_matrix = read_matrix_from_file("first_matrix.txt")
print_matrix(first_matrix)

print("\nSecond Matrix:")
second_matrix = read_matrix_from_file("second_matrix.txt")
print_matrix(second_matrix)

# add the matrices, check if the input is correct, print result
print("\nFirst + Second:")
try:
    resulting_matrix = add_two_matrices(first_matrix, second_matrix)
    print_matrix(resulting_matrix)
    write_matrix_into_file(resulting_matrix, "resulting_matrix.txt")
except WrongSize as error:
    print(error)
    file = open("resulting_matrix.txt", 'w')
    file.write(str(error))
    file.close()
