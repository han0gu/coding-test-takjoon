from functools import cmp_to_key

def compare(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    
    if l1 == l2:
        return int(s1) - int(s2)
    elif l1 > l2:
        s2 += s2[-1] * (l1 - l2)
        return int(s1) - int(s2)
    else:
        s1 += s1[-1] * (l2 - l1)
        return int(s1) - int(s2)

def solution(numbers):
    ls = [str(x) for x in numbers]
    # print('ls', ls)
    
    ls.sort(key=cmp_to_key(compare), reverse=True)
    # print('ls', ls)
    
    return ''.join(ls) if ls[0] != '0' else '0'