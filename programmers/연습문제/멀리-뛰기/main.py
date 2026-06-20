"""
3
-> 1에서 +2
-> 2에서 +1

4
-> 3에서 +1
-> 2에서 +2
"""
def solution(n):
    if n <= 2:
        return n
    
    a = 1
    b = 2
    for i in range(3, n + 1):
        tmp = b
        b += a
        a = tmp
        
    return b % 1234567
