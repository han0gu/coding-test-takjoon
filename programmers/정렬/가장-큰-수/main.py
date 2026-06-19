from functools import cmp_to_key

def compare(s1, s2):
    return int(s1 + s2) - int(s2 + s1)

def solution(numbers):
    ls = [str(x) for x in numbers]
    # print('ls', ls)
    
    ls.sort(key=cmp_to_key(compare), reverse=True)
    # print('ls', ls)
    
    return ''.join(ls) if ls[0] != '0' else '0'