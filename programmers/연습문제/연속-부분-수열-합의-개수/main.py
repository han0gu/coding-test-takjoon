def solution(elements):
    answer = set(elements)
    
    n = len(elements)
    new_elements = elements * 2
    
    for i in range(2, n+1):
        tmp = sum(new_elements[0: i])
        answer.add(tmp)
        
        for j in range(n-1):
            tmp += new_elements[i+j] - new_elements[j]
            answer.add(tmp)
    
    return len(answer)