"""
1 <= r행 c열 <= 400
"""
"""
python3 '문제집/완전탐색/2508-사탕-박사-고창영/main.py' << 'EOF'
2

5 4
.>o<
v.^.
ooo.
^.^.
>o<<

5 4
.>o<
v.^.
ooo.
^.^.
>o<<
EOF
"""

t = int(input())

def check(boxes, row, col):
    row_limit = len(boxes)
    col_limit = len(boxes[0])

    if boxes[row][col] == 'o':
        if (row-1 >= 0 and boxes[row-1][col] == 'v') and (row+1 <= row_limit-1 and boxes[row+1][col] == '^'):
            return 1
        if (col-1 >= 0 and boxes[row][col-1] == ">") and (col+1 <= col_limit-1 and boxes[row][col+1] == "<"):
            return 1

    return 0

for k in range(t):
    input()
    row_limit, col_limit = map(int, input().split())

    boxes = [input() for _ in range(row_limit)]
    # print("boxes", boxes)

    answer = 0
    for row in range(row_limit):
        for col in range(col_limit):
            answer += check(boxes, row, col)

    print(answer)
