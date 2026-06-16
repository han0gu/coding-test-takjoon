from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0, numbers[0]), (0, -numbers[0])]) # (index, acc)
    
    while q:
        i, acc = q.popleft()
        
        if i < len(numbers) - 1:
            q.append( (i+1, acc + numbers[i+1]) )
            q.append( (i+1, acc - numbers[i+1]) )
        elif acc == target:
            answer += 1
        
    return answer