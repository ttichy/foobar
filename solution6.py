from time import time
import timeit


def shortcut(x,y):
    bigger = max(x,y)
    smaller = min(x, y)
    if smaller !=1 and bigger != 1:
        div = bigger / smaller
        left = bigger % smaller
    else:
        div=bigger-1
        left=1

    return (div,left)


def reduce(x,y,count=0):
    if x * y == 1:
        return str(count)
    if y == 0: return 'impossible'

    if y==1: return str(count+x-1)

    if abs(x-y)==1:
        return str(count+y)
    
    div = x // y
    left = x % y
    count +=div

    if left > y:
        return reduce(left,y,count)
    return reduce(y,left,count)


    # if x>y:
    #     div=x // y
    #     left = x % y
    #     return reduce(y,left,count+div)
    # else:
    #     div = y // x
    #     left = y % x
    #     return reduce(x,left,count+div)

    # bigger = max(x,y)
    # smaller = min(x, y)
    # if smaller !=1 and bigger != 1:
    #     div = bigger // smaller
    #     left = bigger % smaller
    # else:
    #     # shortcut cases like 998:1, otherwise stack gets busted
    #     # div=bigger-1
    #     # left=1
    #     return (str(count+bigger-1))
    count +=div
    return reduce(smaller,left,count)


def solution(M,F):
    # type: (str,str)->str
    if M == F: return 'impossible'
    macs = int(M)
    facs = int(F)

    larger = max(macs,facs)
    smaller = min(macs,facs)    
    return reduce(larger,smaller)

def solution2(M, F):
    goal = (int(M), int(F))
    x, y = goal
    c = 0
    while x!=y:
        if x > y:
            num_subs = (x-y)//y + ((x-y) % y > 0)
            c += num_subs
            x, y = x - num_subs * y, y
        elif y > x:
            num_subs = (y-x)//x + ((y-x) % x > 0)
            c += num_subs
            x, y = x, y - num_subs * x
        
    return str(c) if (x, y)==(1, 1) else 'impossible'



def timing(M,F):
    t0=timeit.default_timer()
    print(solution(M,F))
    print('mine elapsed: {}'.format(timeit.default_timer()-t0))

    t0=timeit.default_timer()
    print(solution2(M,F))
    print('his elapsed: {}'.format(timeit.default_timer()-t0))