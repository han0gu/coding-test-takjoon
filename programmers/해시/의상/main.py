"""
카테고리별 1개까지 가능
아무거나 1개 이상 입으면 됨
입는 순서는 의미가 없음

같은 이름의 의상 없음
전체 의상 1~30개
"""
from collections import Counter
from itertools import combinations
import math

def solution(clothes):
    answer = 0
    
    # 카테고리별로 dict 생성
    category_dict = Counter([c[1] for c in clothes])
    # print('category_dict', category_dict)
    
    
    # 1,2,3, ... , n개의 카테고리를 선택하는 모든 경우의 수(tuple)를 구함
    keys = category_dict.keys()
    for i in range(len(keys)):
        for comb in combinations(keys, i+1):
            # print('comb', comb)
            
            cnt = math.prod([category_dict[x] for x in comb])
            # print('cnt', cnt)
            
            answer += cnt

    return answer