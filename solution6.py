def reduce(x,y,count=0):
    if x * y == 1:
        return str(count)
    if y == 0: return 'impossible'
    bigger = max(x,y)
    smaller = min(x, y)
    if smaller !=1 and bigger != 1:
        div = bigger / smaller
        left = bigger % smaller
    else:
        div=1
        left=bigger-smaller
    count=count+div
    return reduce(smaller,left,count)


def solution(M,F):
    # type: (str,str)->str
    if M == F: return 'impossible'
    macs = int(float(M.replace('^','E')))
    facs = int(float(F.replace('^','E')))
   
    return reduce(macs,facs)

