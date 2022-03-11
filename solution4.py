
def solution(l):
    if len(l)==2:
        return 0
    count=0
    pd=[0]*len(l)
    for i in range(0,len(l)):
        for j in range(0,i):
            if l[i] % l[j] == 0:
                pd[i]=pd[i]+1
                count=count+pd[j]

    return count
    



def solution2(l):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        j=0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count