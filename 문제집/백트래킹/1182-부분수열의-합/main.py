n, target = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

stack = [(0, nums[0]), (0, 0)]

while stack:
    idx, value = stack.pop()

    if idx == n-1:
        if value == target:
            answer += 1
        continue
    
    stack.append( (idx + 1, value + nums[idx+1]) )
    stack.append( (idx + 1, value) )
    
print(answer if target != 0 else answer - 1)