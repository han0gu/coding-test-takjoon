from collections import Counter

def solution(phone_book):
    prefix_candidates = Counter(phone_book)
    # print('prefix_candidates', prefix_candidates)
    
    for p in phone_book:
        for i in range(1, len(p)):
            if p[0:i] in prefix_candidates:
                return False
    
    return True