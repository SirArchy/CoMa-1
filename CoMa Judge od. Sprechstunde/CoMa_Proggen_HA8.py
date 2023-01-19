def multiply(A,B):
    matrix_A = convert_string_to_matrix(A)
    matrix_B = convert_string_to_matrix(B)
    result = zeros_matrix(len(matrix_A), len(matrix_B[0]))
    for i in range(len(matrix_A)): # iterate through rows of A
        for j in range(len(matrix_B[0])): # iterate through columns of B
            for k in range(len(matrix_B)):
                temp_result = matrix_A[i][k] + matrix_B[k][j]
                if result[i][j] == 0:
                    result[i][j] = temp_result
                elif temp_result < result[i][j]:
                    result[i][j] = temp_result
    result_string = convert_matrix_to_string(result)
    return result_string


def power(A,m): #das funktioniert noch nich
    matrix_A = convert_string_to_matrix(A)
    end_matrix = zeros_matrix(len(matrix_A), len(matrix_A[0]))
    if m == 2:
        for i in range(len(matrix_A)): # iterate through columns of A
            for j in range(len(matrix_A[0])): # iterate through rows of A
                for k in range(len(matrix_A)):
                    temp_result = matrix_A[i][k] + matrix_A[k][j]
                    if end_matrix[i][j] == 0:
                        end_matrix[i][j] = temp_result
                    elif temp_result < end_matrix[i][j]:
                        end_matrix[i][j] = temp_result
        result_string = convert_matrix_to_string(end_matrix)
        return result_string

    for h in range(m-1):
        temp_matrix = zeros_matrix(len(matrix_A), len(matrix_A[0]))
        if h == 0:
            for i in range(len(matrix_A)): # iterate through columns of A
                for j in range(len(matrix_A[0])): # iterate through rows of A
                    for k in range(len(matrix_A)):
                        temp_result = matrix_A[i][k] + matrix_A[k][j]
                        if end_matrix[i][j] == 0:
                            end_matrix[i][j] = temp_result
                        elif temp_result < end_matrix[i][j]:
                            end_matrix[i][j] = temp_result

        else:
            for i in range(len(matrix_A)): # iterate through columns of A
                for j in range(len(matrix_A[0])): # iterate through rows of A
                    for k in range(len(matrix_A)):
                        temp_result = matrix_A[i][k] + end_matrix[k][j]
                        if temp_matrix[i][j] == 0:
                            temp_matrix[i][j] = temp_result
                        elif temp_result < temp_matrix[i][j]:
                            temp_matrix[i][j] = temp_result
            end_matrix = temp_matrix
    result_string = convert_matrix_to_string(temp_matrix)
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
    for i in range(len(matrix)):
        s += str(matrix[i]).replace(',', '')
        if i != len(matrix) -1: 
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


#Output : ""
#Erwarteter Output: "4 8 6 10, 8 6 9 9, 6 8 4 7, 7 6 9 9"

"""
A = "7, 2, 9, 9"
B = "1 2 8"
print(multiply(A, B))

A = '4 3, 1 7'
B = '2 5 9, 8 6 1'
print(multiply(A, B)) # '6 9 4, 3 6 8'
print(power(A, 4)) # '8 7, 5 8'
print(multiply('9, 3, 1, 5', '8 5'))
print(multiply('9 6 6 10, 2 4 4 6, 3 10 3 10, 4 7 5 2','9 6 6 10, 2 4 4 6, 3 10 3 10, 4 7 5 2'))
"""
