

def power_output(p1,p2):
    if p2 == 0:
        return p1
    return p1*p2

def massage_array(array):
    new_array=[]
    largest_negative = -9999
    count_negatives=0
    for n in array:
        if n < 0 and n > largest_negative:
            largest_negative=n
        if n<0:
            count_negatives=count_negatives+1
        if n!=0: 
            new_array.append(n)

    if count_negatives % 2 == 1:
        new_array.remove(largest_negative)
    return new_array

def solution(array):

    if len(array)==1 and array[0] < 0: return str(array[0])

    mod_array = massage_array(array)
    if len(mod_array)==0: return "0"


    return str(reduce(power_output,mod_array, 1))



