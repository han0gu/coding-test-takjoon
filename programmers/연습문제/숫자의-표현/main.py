def solution(n):
    answer = 0
    
    stack = [(0,0)] # 검토한 수, 누적 합
    
    while stack:
        cur_n, acc = stack.pop()
        
        if acc > n:
            continue
    
        if acc == n:
            answer += 1
            continue
            
        if cur_n == n:
            continue
            
        stack.append((cur_n + 1, acc))
        stack.append((cur_n + 1, acc + cur_n + 1))
    
    return answer