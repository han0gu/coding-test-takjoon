from itertools import combinations

n, target = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

for i in range(1,n+1):
    for c in combinations(nums, i):
        if sum(c) == target:
            answer += 1

print(answer)
