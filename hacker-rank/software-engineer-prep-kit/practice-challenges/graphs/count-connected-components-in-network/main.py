#!/bin/python3

#
# Complete the 'countIsolatedCommunicationGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY links
#  2. INTEGER n
#

"""
0 1
1 0
"""

"""
0 1 0 0
1 0 0 0
0 0 0 1
0 0 1 0
"""

"""
0 1 1
1 0 1
1 1 0
"""

def paint_with_one(board, start, end):
    board[start][end] = 1
    board[end][start] = 1
    
def add_near(board, row, col, stack):
    if 0 <= row < n and 0 <= col < n and board[row][col] == 1:
        stack.append((row, col))
    
def countIsolatedCommunicationGroups(links, n):
    
    if not links:
        return 0
        
    if n == 1:
        return 1
        
    answer = 0
    
    board = [[0] * n for _ in range(n)]
    # print('init board', board)
    
    for start, end in links:
        paint_with_one(board, start, end)
    # print('paint board', board)
    
    stack = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                answer += 1
                stack.append((row, col))
                # print('init stack', stack)
                
                while stack:
                    row, col = stack.pop()
                    board[row][col] = 0
                    
                    add_near(board, row, col+1, stack)
                    add_near(board, row+1, col-1, stack)
                    add_near(board, row+1, col, stack)
                    add_near(board, row+1, col+1, stack)
                    # print('stack', stack)
                    
            # print('board', board)
                
    return answer

if __name__ == '__main__':
    links_rows = int(input().strip())
    links_columns = int(input().strip())

    links = []

    for _ in range(links_rows):
        links.append(list(map(int, input().rstrip().split())))

    n = int(input().strip())

    result = countIsolatedCommunicationGroups(links, n)

    print(result)
