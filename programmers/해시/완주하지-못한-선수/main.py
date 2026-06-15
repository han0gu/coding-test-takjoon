from collections import Counter

def solution(participant, completion):
    c1 = Counter(participant)
    c2 = Counter(completion)
    
    for key in c1:
        v1 = c1[key]
        v2 = c2[key]
        if v1 != v2:
            return key