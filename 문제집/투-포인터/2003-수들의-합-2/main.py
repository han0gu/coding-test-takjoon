"""
1 ≤ N ≤ 10,000

1 ≤ M ≤ 300,000,000

1 <= A[x] <= 30,000

"""

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# print('numbers', numbers)

answer = 0

for i in range(n):
    total = numbers[i]
    if total == m:
        answer += 1
        continue
    
    for j in range(i + 1, n):
        total += numbers[j]
        
        if total > m:
            break
        elif total == m:
            answer += 1
            break
        else:
            continue

print(answer)