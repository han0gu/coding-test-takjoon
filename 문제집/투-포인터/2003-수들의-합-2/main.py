"""
1 ≤ N ≤ 10,000

1 ≤ M ≤ 300,000,000

1 <= A[x] <= 30,000

"""

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# print('numbers', numbers)

answer = 0
start = 0
end = 0
while start <= end and end <= n - 1:
    total = sum(numbers[start:end+1])

    if start == end:
        if total == m:
            answer += 1
            start += 1
            end += 1
        elif total > m:
            start += 1
            end += 1
        else:
            end += 1
    else:
        if total == m:
            answer += 1
            start += 1
            end += 1
        elif total > m:
            start += 1
        else:
            end += 1

print(answer)
