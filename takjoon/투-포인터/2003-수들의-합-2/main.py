"""
1 ≤ N ≤ 10,000

1 ≤ M ≤ 300,000,000

1 <= A[x] <= 30,000

"""

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# print('numbers', numbers)

answer = 0
end = 0
total = 0

for start in range(n):
    while end < n and total < m:
        total += numbers[end]
        end += 1

    if total == m:
        answer += 1

    total -= numbers[start]

print(answer)
