"""
원소의 개수가 1~n개인 모든 부분집합을 구함

원소의 개수가 k개인 부분집합을 구할 때는 k-1개인 부분집합의 결과를 재활용함
"""
n, target = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

# 개수가 1개
candidates = {}
candidates[1] = [*nums]
# print('candidates', candidates)

# 개수가 2 ~ n개인 부분집합 계산
for k in range(1, n): # 1~4
    reuse = candidates[k]
    # print('reuse', reuse)

    candidates[k+1] = [] # 2, 3, 4
    
    r = range(k, n) # 1~4, 2~4, 3~4, 4
    for i in r:
        candidates[k+1].append(reuse[i-k] + nums[i])
# print('candidates', candidates)

for nums in candidates.values():
    for n in nums:
        if n == target:
            answer += 1

print(answer)
