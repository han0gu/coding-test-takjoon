def solution(maps):
    answer = -1
    
    n = len(maps)
    m = len(maps[0])
    
    stack = [(0,0,1)]
    visited = [[False] * m for _ in range(n)]
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    
    while stack:
        row, col, acc = stack.pop()
        
        if visited[row][col]:
            continue
        
        visited[row][col] = True
        
        if row == n - 1 and col == m - 1:
            answer = acc if answer == -1 else min(answer, acc)
        
        for d_r, d_c in directions:
            new_r = row + d_r
            new_c = col + d_c
            
            if (0 <= new_r < n and 
                0 <= new_c < m and 
                maps[new_r][new_c] == 1 and 
                not visited[new_r][new_c]):
                stack.append((new_r, new_c, acc + 1))
                
    return answer