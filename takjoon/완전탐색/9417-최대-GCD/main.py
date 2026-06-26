"""
테스트 케이스의 개수 N (1 < N < 100)

양의 정수 M (1 < M < 100)개가 주어진다

모든 수는 `-2^31`보다 크거나 같고, `2^31 - 1`보다 작거나 같다.
"""
import math

n = int(input())
test_cases = [list(map(int, input().split())) for _ in range(n)]
# print('test_cases', test_cases)

for case in test_cases:
    answer = 1

    for i in range(len(case)):
        for j in range(i + 1, len(case)):
            answer = max(answer, math.gcd(case[i], case[j]))

    print(answer)

"""
1
125 15 25

"""
