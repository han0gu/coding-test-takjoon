"""
카테고리별 1개까지 가능
아무거나 1개 이상 입으면 됨
입는 순서는 의미가 없음

같은 이름의 의상 없음
전체 의상 1~30개
"""
from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    
    # 카테고리별로 dict 생성
    category_dict = defaultdict(list)
    for clth, cate in clothes:
        category_dict[cate].append(clth)
    # print('category_dict', category_dict)
    
    
    # 1,2,3, ... , n개의 카테고리를 선택하는 모든 경우의 수(tuple)를 구함
    keys = category_dict.keys()
    all_combs = []
    for i in range(len(keys)):
        all_combs.extend(combinations(keys, i+1))
    # print('all_combs', all_combs)
    
    
    # 각 카테고리에 포함된 의상의 개수를 곱셈
    for comb in all_combs:
        cnt = 1
        for c in comb:
            cnt *= len(category_dict[c])
        answer += cnt
    
    return answer