"""
완전 탐색은 O(n^2) -> 스택/큐/해시 등

가격이 떨어지지 않은 인덱스들은 나중에 한번에 역산할 수 있다 -> 가격이 떨어지는 순간 즉시 계산/업데이트 한다
"""
def solution(prices):
    answer = [0] * len(prices)
    remain_indices = [] # 아직 가격이 떨어지지 않은 인덱스들
    
    for i, p in enumerate(prices):
        # 가격이 내려가는 순간 즉시 계산/업데이트
        while remain_indices and prices[remain_indices[-1]] > p:
            top = remain_indices.pop()
            answer[top] = i - top
        
        remain_indices.append(i)
    
    for i in remain_indices:
        answer[i] = len(prices) - 1 - i
        
    return answer
