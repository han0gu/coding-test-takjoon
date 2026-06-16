def solution(arr):
    answer = []
    
    for n in arr:
        if not answer:
            answer.append(n)
        elif answer[-1] != n:
            answer.append(n)
            
    return answer