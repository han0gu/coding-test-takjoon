"""
여자 N / 0~100
남자 M / 0~100
K명은 반드시 인턴 / 0~200
인턴은 대회 참가 못함
"""

n, m, k = map(int, input().split())

for _ in range(k):
    if n >= m*2:
        n -= 1
    else:
        m -= 1

print(min(n//2, m))