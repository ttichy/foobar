
def pair_up(macs, facs):
    '''
    returns number of pairs and how many are left over
    '''
    diff = macs - facs
    abs_diff=abs(diff)
    pairs = max(macs,facs)-abs_diff

    return (pairs,abs_diff)


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



def prev(pairs, leftovers, count=0):
    
    if pairs !=1 and leftovers !=1:
        if max(pairs,leftovers) % min(pairs,leftovers)==0:
            return 'impossible'
    
    if pairs==1 and leftovers == 0:
        return count-1
    diff = abs(pairs-leftovers)
    smaller = min(pairs,leftovers)
    return prev(diff,smaller,count+1)


def solution_old(M,F):
    if M == F: return 'impossible'
    # type: (str,str)->str
    macs = int(float(M.replace('^','E')))
    facs = int(float(F.replace('^','E')))



    (pairs,leftovers) = pair_up(macs,facs)

    # do this check only if both not one, otherwise it fails when it should not
    if pairs !=1 and leftovers !=1:
        if max(pairs,leftovers) % min(pairs,leftovers)==0:
            return 'impossible'

    (short,left) = shortcut(pairs,leftovers)

    result = prev(left,min(pairs,leftovers))
    if result=='impossible': return 'impossible'

    return str(result+short)

def solution (M,F):
    # type: (str,str)->str
    if M == F: return 'impossible'
    macs = int(float(M.replace('^','E')))
    facs = int(float(F.replace('^','E')))
    x = facs
    y = macs
    steps = 0
    while x * y != 1:
        if facs==macs: return 'impossible'

        (count,leftover)=shortcut(x,y)
        if leftover==0: return 'impossible'
        x=min(x,y)
        y=leftover
        steps = steps+count

    return str(steps)

