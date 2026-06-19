from collections import deque

def solution(tickets):
    answer = []
    n = len(tickets)

    q = deque([('ICN', 0, [False] * n, ['ICN'])]) # (도착지, 사용한 티켓 개수, 티켓 사용 여부 리스트, answer)
    
    while q:
        cur_e, used_cnt, visited, cur_answer = q.popleft()
        
        if used_cnt == n:
            answer.append(cur_answer)
            continue
        
        for i, (nxt_s, nxt_e) in enumerate(tickets):
            if not visited[i] and cur_e == nxt_s:
                new_visited = [*visited]
                new_answer = [*cur_answer]
                
                new_visited[i] = True
                new_answer.append(nxt_e)
                
                q.append( (nxt_e, used_cnt + 1, new_visited, new_answer) )
    
    return min(answer)