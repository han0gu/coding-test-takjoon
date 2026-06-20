def solution(people, limit):    
    answer = 0
    
    people.sort(reverse=True)
    n = len(people)
    rescued = [False] * n
    rescued_cnt = 0
    
    while rescued_cnt < n:
        answer += 1
        boat = 0
        boat_p_cnt = 0
        
        for i in range(n):
            if not rescued[i] and boat + people[i] <= limit:
                rescued[i] = True
                rescued_cnt += 1
                
                boat += people[i]
                boat_p_cnt += 1
                if boat_p_cnt == 2:
                    break
        
    return answer