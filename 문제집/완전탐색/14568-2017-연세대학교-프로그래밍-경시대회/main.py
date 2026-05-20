"""
python3 '문제집/완전탐색/14568-2017-연세대학교-프로그래밍-경시대회/main.py' << 'EOF'
7
EOF
"""

"""
총 사탕 수 N = 1~100

모두 자연수 개의 사탕을 받음

택희 = 짝수(최소 2개)
남규 >= 영훈 + 2
"""
n = int(input())

if n < 6:
    print(0)
if n == 6:
    print(1)
if n > 6:
    answer = []

    # 택희 먼저 결정
    for i in range(1, int(n/2)):
        a = i*2
        exclude_a = n - a

        # 남규 + 영훈의 최소값은 3이므로
        if exclude_a < 3:
            continue

        # 남규/영훈 계산
        for b in range(exclude_a - 1, 2, -1):
            c = exclude_a - b
            
            if b >= c + 2:
                answer.append([a, b, c])

    print(len(answer))