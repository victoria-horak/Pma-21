def read_matrix(file_name, column, row):
    with open(file_name, "r") as file:
        matrix = []
        for line in file:
            list = [x for x in line.strip().split(",")]
            list = [int(x) for x in list if x]
            matrix.append(list)
        matrix = [x for x in matrix if x]
        result = []
        for iterator in range(0, column):
            rows = []
            for jterator in range(0, row):
                rows.append(0)
            result.append(rows)
        for iterator in range(0, column):
            for jterator in range(0, row):
                result[iterator][jterator] = matrix[iterator][jterator]
    file.close()
    return result


def read_vector_static(file_name):
    with open(file_name, "r") as file:
        list_for_vector = []
        for line in file:
            for x in line.strip().split(','):
                list_for_vector.append(x)
        list_for_vector = [x for x in list_for_vector if x]
        list_for_vector = [int(x) for x in list_for_vector if x]
    return list_for_vector


