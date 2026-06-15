from collections import Counter

def solution(participant, completion):
    c1 = Counter(participant)
    c2 = Counter(completion)
    
    diff = c1 - c2
    # print('diff', diff)
    
    keys = diff.keys()
    # print('keys', keys)

    return list(keys)[0]
        
p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]
solution(p, c)