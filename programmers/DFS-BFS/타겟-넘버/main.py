def solution(numbers, target):
    answer = 0
    stack = [(0, numbers[0]), (0, -numbers[0])] # (index, acc)
    
    while stack:
        i, acc = stack.pop()
        
        if i < len(numbers) - 1:
            stack.append( (i+1, acc + numbers[i+1]) )
            stack.append( (i+1, acc - numbers[i+1]) )
        elif acc == target:
            answer += 1
        
    return answer