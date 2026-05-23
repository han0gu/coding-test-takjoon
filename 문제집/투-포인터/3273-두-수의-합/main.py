"""
1 ≤ n ≤ 100,000, 

1 ≤ ai ≤ 1,000,000, 

1 ≤ x ≤ 2,000,000
"""
from itertools import combinations

n = int(input())

numbers = list(map(int, input().split()))
# print('numbers', numbers)

x = int(input())

answer = 0
for a, b in combinations(numbers, 2):
    if a + b == x:
        # print(a + b)
        answer += 1

print(answer)