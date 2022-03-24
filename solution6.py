
def pair_up(macs, facs):
    '''
    returns number of pairs and how many are left over
    '''
    diff = macs - facs
    abs_diff=abs(diff)
    pairs = max(macs,facs)-abs_diff

    return (pairs,abs_diff)


def shortcut(pairs, leftovers):
    bigger = max(pairs,leftovers)
    smaller = min(pairs, leftovers)
    
    div = bigger / smaller
    count = bigger % smaller

    return(div,count)



def prev(pairs, leftovers, count=0):
    
    if pairs !=1 and leftovers !=1:
        if max(pairs,leftovers) % min(pairs,leftovers)==0:
            return 'impossible'
    
    if pairs==1 and leftovers == 0:
        return count-1
    diff = abs(pairs-leftovers)
    smaller = min(pairs,leftovers)
    return prev(diff,smaller,count+1)


def solution(M,F):
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
