def multiply(A,B):
    matrix_A = convert_string_to_matrix(A)
    matrix_B = convert_string_to_matrix(B)
    result = zeros_matrix(len(matrix_A), len(matrix_B[0]))
    for i in range(len(matrix_A)): # iterate through columns of B
        for j in range(len(matrix_B[0])): # iterate through rows of B
            for k in range(len(matrix_B)):
                if result[i][j] == 0:
                    result[i][j] = matrix_A[i][k] + matrix_B[k][j]
                elif matrix_A[i][k] + matrix_B[k][j] < result[i][j]:
                    result[i][j] = matrix_A[i][k] + matrix_B[k][j]
    result_string = convert_matrix_to_string(result)
    return result_string


def power(A,m):
    matrix_A = convert_string_to_matrix(A)
    result = zeros_matrix(len(matrix_A), len(matrix_A[0]))
    subl = []
    end_result = zeros_matrix(len(matrix_A), len(matrix_A[0]))
    for h in range(m-1):
        if h > 1:
            result = end_result
            end_result = zeros_matrix(len(matrix_A), len(matrix_A[0]))
        for i in range(len(matrix_A)): # iterate through columns of B
            for j in range(len(matrix_A[0])): # iterate through rows of B
                for k in range(len(matrix_A)):
                    if h == 0:
                        subl.append(matrix_A[i][k] + matrix_A[k][j])
                    else:
                        subl.append(result[i][k] + matrix_A[k][j])
                if h == 0:
                    result[i][j] = min(subl)
                    subl = []
                else:
                    end_result[i][j] = min(subl)
                    subl = []
    result_string = convert_matrix_to_string(end_result)
    return result_string


def convert_string_to_matrix(string):
    matrix_A = string.split(",")
    matrix_A_list = []
    for item in matrix_A:
        subl = []
        for num in item.split():
            subl.append(int(num))
        matrix_A_list.append(subl)
    return matrix_A_list


def convert_matrix_to_string(matrix):
    s = ''
    for item in matrix:
        s += str(item).replace(',', '')
        if item != matrix[-1]:
            s += ', '
    string_matrix = s.replace('[', '').replace(']', '')
    return string_matrix


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0)

    return M




"""
A = '4 3, 1 7'
B = '2 5 9, 8 6 1'
print(multiply(A, B)) # '6 9 4, 3 6 8'
print(power(A, 4)) # '8 7, 5 8'
print(multiply('9, 3, 1, 5', '8 5'))
print(multiply('9 6 6 10, 2 4 4 6, 3 10 3 10, 4 7 5 2','9 6 6 10, 2 4 4 6, 3 10 3 10, 4 7 5 2'))
"""
