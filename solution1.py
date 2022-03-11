
# given substring, see if it can be repeated
def check_substring(str, substr):
    if not str:
        return True
    if str[:len(substr)]!=substr:
        return False
    return check_substring(str[len(substr):],substr)



def solution(str):
    length = len(str)
    rng = range(1,length-1)
    for size in rng:
        # don't bother checking if there is reminder
        if length % size != 0:
            continue
        substr=str[:size]

        if check_substring(str,substr):
            return int(len(str)/len(substr))

    # worst case there is only one equal part (the whole cake)    
    return 1

