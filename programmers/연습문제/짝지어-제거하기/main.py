def solution(s):
    
    stack = [s[0]]
    
    for c in s[1:]:
        if not stack:
            stack.append(c)
        
        head = stack[-1]
        if head == c:
            stack.pop()
        else:
            stack.append(c)
            
    return 1 if not stack else 0