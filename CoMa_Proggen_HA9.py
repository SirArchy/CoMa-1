def LU_decomposition(A):
    A = convert_string_to_matrix(A)
    n = len(A)

    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]
 
    """Decomposing matrix into Upper
     and Lower triangular matrix"""
    for i in range(n):
 
        # Upper Triangular
        for k in range(i, n):
 
            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
 
            # Evaluating U(i, k)
            upper[i][k] = A[i][k] - sum
 
        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:
 
                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
 
                # Evaluating L(k, i)
                lower[k][i] = int((A[k][i] - sum) /
                                  upper[i][i])
    
    #combine both matrices
    LU = upper
    for l in range(1,len(lower)):
        for m in range(l):
            LU[l][m] = lower[l][m]
    return convert_matrix_to_string(LU)

def solve_LGS(A,B):
    LU = convert_string_to_matrix(LU_decomposition(A))
    A = convert_string_to_matrix(A)
    B = convert_string_to_matrix(B)

    #divide L and U for forward/backward substitution
    n = len(A)
    
    L = [[0 for x in range(n)]
             for y in range(n)]
    for i in range(1,len(LU)):
        for j in range(i):
            L[i][j] = LU[i][j]
    for h in range(len(A)):
        L[h][h] = 1

    U = LU
    for i in range(1,len(LU)):
        for j in range(i):
            U[i][j] = 0

    #solve Lx=b to get x
    Y = forward_substitution(L,B)

    #solve Ux=y to get y
    X = back_substitution(U,Y)

    return convert_matrix_to_string(X)

def forward_substitution(L, b):
    
    #Get number of rows for L
    n = len(L)
    
    #Allocating space for the solution vector
    y = [[0 for x in range(len(b[0]))]
             for y in range(len(b))]
    
    for i in range (1,n):
        sum = 0
        for j in range (i):
            sum += L[i][j]*y[j]
        y[i] = (b[i]-sum)/L[i][i] 
        
    return y


def back_substitution(U, y):
    
    #Get number of rows for U
    n = len(U)
    
    #Allocating space for the solution vector
    x = [[0 for i in range(y[0])]
             for j in range(y)]

    for i in range(n-1, -1, -1):
        tmp = y[i]
        for j in range(n-1, i, -1):
            tmp -= x[j]*U[i,j]
            
        x[i] = tmp/U[i,i]
        
    return x


def dot_product(A, B): #NOT WORKING!!!
    """
    Perform a dot product of two vectors or matrices
        :param A: The first vector or matrix
        :param B: The second vector or matrix
    """
    # Ensure A and B dimensions are the same
    rowsA = len(A)
    colsB = len(B[0])

    # Sum the products
    total = 0
    for i in range(rowsA):
        for j in range(colsB):
            total += A[i][j] * B[i][j]

    return total


def multiply(A,B):
    n = len(A)
    result = [[0 for x in range(n)]
             for y in range(n)]
    for i in range(len(A)): # iterate through rows of A
        for j in range(len(B[0])): # iterate through columns of B
            for k in range(len(B)):
                temp_result = A[i][k] + B[k][j]
                if result[i][j] == 0:
                    result[i][j] = temp_result
                elif temp_result < result[i][j]:
                    result[i][j] = temp_result
    return result

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

"""
y = '-1 7, 2 -18, -26 116'
L = '2 4 -7, -4 -7 13, 34 71 -131'
y = convert_string_to_matrix(y)
L = convert_string_to_matrix(L)

print(L[2][:2])
print(y[:2])
"""
 
print(solve_LGS('2 4 -7, -4 -7 13, 34 71 -131','-1 7, 2 -18, -26 116')) #'1 10, 1 -5, 1 -1'
print(solve_LGS('5 -3, 35 -29','13 15 -8, 99 25 -64')) #'2 9 -1, -1 10 1'
print(solve_LGS('17 4, -17 42','81, -127')) #'5, -1'