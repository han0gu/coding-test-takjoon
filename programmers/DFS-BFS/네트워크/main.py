"""
BFS

특정 노드를 pop, 방문 처리, answer += 1
-> 인접 노드를 append
-> queue가 빈 경우 네크워크 하나 끝
"""
from collections import deque

def solution(n, computers):
    answer = 0
    
    row_cnt = len(computers)
    col_cnt = len(computers[0])
    
    visited = [[False] * col_cnt for _ in range(row_cnt)]
    
    q = deque()
    
    for r in range(row_cnt):
        for c in range(col_cnt):
            # 네트워크 시작점 등록
            if not visited[r][c] and computers[r][c] == 1:
                q.append((r,c))
                answer += 1
                # print('start', r, c)
            
            # 인접 노드 처리
            while q:
                # 시작점 처리
                cur_r, cur_c = q.popleft()
                visited[cur_r][cur_c] = True
                visited[cur_c][cur_r] = True
                
                # 시작점에 연결된 모든 노드 처리
                for i in range(col_cnt):
                    if not visited[cur_r][i] and computers[cur_r][i] == 1:
                        # print('near', cur_r, i)
                        q.append((cur_r, i))
                        q.append((i, cur_r))   
            
    return answer