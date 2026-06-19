def solution(tickets):
    tickets.sort()
    
    n = len(tickets)
    visited = [False] * n
    route = ["ICN"]
    
    def dfs(cur_airport):
        if len(route) == n + 1:
            return True
        
        for i, (start, end) in enumerate(tickets):
            if not visited[i] and start == cur_airport:
                visited[i] = True
                route.append(end)
                
                if dfs(end):
                    return True
                
                route.pop()
                visited[i] = False
        
        return False
    
    dfs("ICN")
    return route
