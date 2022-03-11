from fractions import Fraction
from re import T



def zeros_matrix(rows, cols):
    """
    from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
 
        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
 
    return M

def identity_matrix(n):
    """
    from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
 
        :return: a square identity matrix
    """
    IdM = zeros_matrix(n, n)
    for i in range(n):
        IdM[i][i] = 1.0
 
    return IdM

def print_matrix(M, decimals=3):
    """
    Print a matrix one row at a time
        :param M: The matrix to be printed
        from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    """
    for row in M:
        print([round(x,decimals)+0 for x in row])


def transpose(M):
    """
    Returns a transpose of a matrix.
        :param M: The matrix to be transposed
 
        :return: The transpose of the given matrix
    from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/        
    """
    # Section 1: if a 1D array, convert to a 2D array = matrix
    if not isinstance(M[0],list):
        M = [M]
 
    # Section 2: Get dimensions
    rows = len(M)
    cols = len(M[0])
 
    # Section 3: MT is zeros matrix with transposed dimensions
    MT = zeros_matrix(cols, rows)
 
    # Section 4: Copy values from M to it's transpose MT
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]
 
    return MT        

def matrix_subtraction(A, B):
    """
    Subtracts matrix B from matrix A and returns difference
        :param A: The first matrix
        :param B: The second matrix
 
        :return: Matrix difference
        from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    """
    # Section 1: Ensure dimensions are valid for matrix subtraction
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')
 
    # Section 2: Create a new matrix for the matrix difference
    C = zeros_matrix(rowsA, colsB)
 
    # Section 3: Perform element by element subtraction
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]
 
    return C    

def matrix_multiply(A, B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix
 
        :return: The product of the two matrices
        from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')
 
    # Section 2: Store matrix multiplication in a new matrix
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
 
    return C    

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
 
        :return: A copy of the given matrix
        from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    """
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])
 
    # Section 2: Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)
 
    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
 
    return MC

def pre_process_step1(m):
    """
    return a tuple (matrix,[absorbing states])
    """
    rows = len(m)
    cols = len(m[0])
    result = zeros_matrix(rows,cols)
    absorb_states = []
    for i in range(rows):
        row = m[i]
        rowsum=sum(row)
        # if rowsum is zero, mark absorbing state
        if rowsum==0:
            result[i][i]=1
            absorb_states.append(i)
            continue
        for j in range(cols):
            result[i][j]=Fraction(m[i][j],rowsum)

    return (result,absorb_states)

def get_R_Q_matrices(m, ab_states):
    """
    Puts m into standard form, returns a new matrix
    """
    ms=zeros_matrix(len(m),len(m[0]))
    ab_states.sort(reverse=True)
    for i in range(len(ab_states)):
        ms[i][i]=1
    print(i)
    ab_set = set(ab_states)
    all_set = set(range(0,len(m)))
    diff = all_set.difference(ab_set)
    states=ab_states+list(diff)
    i=i+1
    q_start_row=i
    r_start_row=i
    r_start_col=i
    for from_st in (states)[i:]:
        for j,to_st in enumerate(states):
            ms[i][j]=m[from_st][to_st]
        i=i+1
    
    Q=zeros_matrix(len(states)-q_start_row,len(ab_states))
    R=zeros_matrix(len(states)-r_start_row, len(states)-len(ab_states))
    for i in range(q_start_row,len(ms[0])):
        for j in range(r_start_col-1):
            Q[i-q_start_row][j]=ms[i][j]
        for k in range(r_start_col,len(ms)):
            R[i-q_start_row][k-r_start_col]=ms[i][k]
    
    return (Q,R)


    

