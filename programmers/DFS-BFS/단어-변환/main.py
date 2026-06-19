from collections import deque

def can_change(w1, w2):
    diff_cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff_cnt += 1
    return diff_cnt == 1

def solution(begin, target, words):
    
    answer = 0
    
    visited = [False] * len(words)
    q = deque([(begin, 0)]) # (현재 단어, 누적 변경 횟수)
    
    while q:
        cur, cnt = q.popleft()
        
        if cur == target:
            answer = min(answer, cnt) if answer != 0 else cnt
            
        for i, w in enumerate(words):
            if not visited[i] and can_change(cur, w):
                visited[i] = True
                q.append((w, cnt + 1))
                
    return answer