"""
python3 '문제집/완전탐색/6131-완전-제곱수/main.py' << 'EOF'
15
EOF
"""

"""
1 ≤ B ≤ A ≤ 500

A^2 = B^2 + N (1 ≤ N ≤ 1,000)
"""

import math

n = int(input())

LIMIT = 500
answer_count = 0
for b in range(1, LIMIT + 1):
    a_square = b ** 2 + n
    a_isqrt = math.isqrt(a_square)

    if a_isqrt ** 2 == a_square and a_isqrt <= LIMIT:
        answer_count += 1

print(answer_count)
