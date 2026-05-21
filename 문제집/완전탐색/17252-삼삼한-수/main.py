"""
0 <= N <= 2,147,483,647
각 수를 한번씩만 더해야 함
"""
"""
python3 '문제집/완전탐색/17252-삼삼한-수/main.py' << 'EOF'
109
EOF

python3 '문제집/완전탐색/17252-삼삼한-수/main.py' << 'EOF'
298
EOF

python3 '문제집/완전탐색/17252-삼삼한-수/main.py' << 'EOF'
0
EOF

python3 '문제집/완전탐색/17252-삼삼한-수/main.py' << 'EOF'
1
EOF
"""

n = int(input())

if n == 0:
    print("NO")
else:
    ternary_digits = ''
    while n > 0:
        ternary_digits += str(n % 3)
        n //= 3
    # print("ternary_digits", ternary_digits)
    print('NO' if ternary_digits.find('2') > -1 else 'YES')