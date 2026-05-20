"""
python3 '문제집/완전탐색/16283-농장/main.py' << 'EOF'
3 4 9 32
EOF

python3 '문제집/완전탐색/16283-농장/main.py' << 'EOF'
3 4 8 32
EOF

python3 '문제집/완전탐색/16283-농장/main.py' << 'EOF'
100 100 2 200
EOF
"""

"""
양
- 사료 A 그램
- 1 ~ 1000 마리

염소
- 사료 B 그램
- 1 ~ 1000 마리

전체 N 마리
- 2 ~ 1000 마리

소비한 사료 W 그램
- 2 ~ 1,000,000 그램
"""

a, b, n, w = map(int, input().split())
# print(a,b,n,w)

# sheep + goat = n
# a * sheep + b * goat = w
answer_count = 0
answer = []
for sheep in range(1, n):
    goat = n - sheep
    if a * sheep + b * goat == w:
        answer_count += 1
        if answer_count >= 2:
            break
        
        answer = [sheep, goat]

if answer_count > 1 or not answer:
    print(-1)
else:
    print(f"{answer[0]} {answer[1]}")