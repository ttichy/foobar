def shortcut(x, y):
    bigger = max(x,y)
    smaller = min(x, y)
    if smaller !=1 and bigger != 1:
        div = bigger / smaller
        left = bigger % smaller
    else:
        div=1
        left=bigger-smaller


    return(div,left)

def solution(M,F):
    # type: (str,str)->str
    if M == F: return 'impossible'
    macs = int(float(M.replace('^','E')))
    facs = int(float(F.replace('^','E')))
    x = facs
    y = macs
    steps = 0
    while x * y != 1:
        if x==y: return 'impossible'

        (count,leftover)=shortcut(x,y)
        if leftover==0: return 'impossible'
        x=min(x,y)
        y=leftover
        steps = steps+count

    return str(steps)

