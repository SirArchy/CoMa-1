import numpy as np

def LU_decomposition(A):
    A = convert_string_to_matrix(A)
    n = len(A)

    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]cd ..
 
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
    Y = forward_sub(L,B)

    #solve Ux=y to get y
    X = back_sub(U,Y)

    return convert_matrix_to_string(X)


def forward_sub(L, b):
    """x = forward_sub(L, b) is the solution to L x = b
       L must be a lower-triangular matrix
       b must be a vector of the same leading dimension as L
    """
    n = L.shape[0]
    x = np.zeros(n)
    for i in range(n):
        tmp = b[i]
        for j in range(i-1):
            tmp -= L[i,j] * x[j]
        x[i] = tmp / L[i,i]
    return x


def back_sub(U, b):
    """x = back_sub(U, b) is the solution to U x = b
       U must be an upper-triangular matrix
       b must be a vector of the same leading dimension as U
    """
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        tmp = b[i]
        for j in range(i+1, n):
            tmp -= U[i,j] * x[j]
        x[i] = tmp / U[i,i]
    return x



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


print(LU_decomposition('2 4 -7, -4 -7 13, 34 71 -131')) #'2 4 -7, -2 1 -1, 17 3 -9'
print(solve_LGS('2 4 -7, -4 -7 13, 34 71 -131','-1 7, 2 -18, -26 116')) #'1 10, 1 -5, 1 -1'
print(LU_decomposition('5 -3, 35 -29')) #'5 -3, 7 -8'
print(solve_LGS('5 -3, 35 -29','13 15 -8, 99 25 -64')) #'2 9 -1, -1 10 1'
print(LU_decomposition('17 4, -17 42')) #'17 4, -1 46'
print(solve_LGS('17 4, -17 42','81, -127')) #'5, -1'

