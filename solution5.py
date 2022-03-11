from fractions import Fraction
import fractions
from operator import inv
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
            M[-1].append(0)
 
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
        IdM[i][i] = 1
 
    return IdM

def print_matrix(M, decimals=3):
    """
    Print a matrix one row at a time
        :param M: The matrix to be printed
        from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    """
    for row in M:
        print([round(x,decimals)+0 for x in row])


def invert_matrix(A, tol=None):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed
 
        :return: The inverse of the matrix A
        modified from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    """
 
    # Section 2: Make copies of A & I, AM & IM, to use for row ops
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)
 
    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        # FIRST: scale fd row with fd inverse. 
        # fdScaler = 1.0 / AM[fd][fd]
        scaler = Fraction(1,AM[fd][fd])
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] = AM[fd][j] * scaler
            # AM[fd][j] *= fdScaler
            IM[fd][j] = IM[fd][j] * scaler
            # IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: 
            # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): 
                # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM


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

def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
 
        :return: a square identity matrix
        from: https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
    """
    IdM = zeros_matrix(n, n)
    for i in range(n):
        IdM[i][i] = 1
 
    return IdM

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
        for j in range(r_start_col):
            Q[i-q_start_row][j]=ms[i][j]
        for k in range(r_start_col,len(ms)):
            R[i-q_start_row][k-r_start_col]=ms[i][k]
    
    return (R,Q,states)

def calc_FR(R,Q):
    I = identity_matrix(len(Q))
    diff = matrix_subtraction(I,Q)

    F = invert_matrix(diff)
    FR = matrix_multiply(F,R)

    return FR

def lcm(a, b):
    return abs(a*b) // fractions.gcd(a, b)

def lcm_multi(array):
    res=1
    for num in array:
        res=lcm(res,num)
    return res

def solution(m):
    (m1,abs_states) = pre_process_step1(m)

    (Q,R,states) = get_R_Q_matrices(m1,abs_states)
    FR = calc_FR(R,Q)

    result_states=states[len(abs_states):]
    # find state 0
    s0=result_states.index(0)

    result_row = FR[s0]

    mydict = {}
    for i,res in enumerate(result_row):
        st=abs_states[i]
        mydict[st]=res

    almost_there=[]
    for key in sorted(mydict):
        almost_there.append(mydict[key])

    numerators = map(lambda x: x.numerator,almost_there)
    denoms = map(lambda x: x.denominator, almost_there)

    lcm = lcm_multi(denoms)

    result=[]
    for i,num in enumerate(numerators):
        fr=lcm / denoms[i]
        result.append(num * fr)
    
    result.append(lcm)
    return result
    

