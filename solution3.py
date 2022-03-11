from fractions import Fraction

def solution(pegs):

    # using a system of N equations and N unknowns and solving with a shortcut
    lhs=pegs[:-1]
    rhs=pegs[1:]

    sum = 0

    for index in range(0,len(lhs)):
        p_left=lhs[index]
        p_right=rhs[index]
        if index % 2 == 0:
            sum=sum+(p_right-p_left)
        else:
            sum=sum+(-p_right+p_left)


    if len(lhs) % 2 == 0:
        denominator = 1
    else:
        denominator = 3

    r_first = 2* sum /denominator
    if r_first < 1:
        return [-1,-1]

    rs = [r_first]

    # need to check for zero length gears
    for n in range(1,len(pegs)-1):
        r_nPlus1 = pegs[n] - pegs[n-1]-rs[n-1]
        rs.append(r_nPlus1)
        if r_nPlus1== 0:
            return [-1,-1]

    fr = Fraction(2*sum,denominator)
    return [fr.numerator,fr.denominator]
