"""
마라톤 코스는 N (3 ≤ N ≤ 100000) 개의 체크포인트

-1000 ≤ x, y ≤ 1000

체크 포인트의 좌표는 겹칠 수도 있다
그 번호의 체크포인트만 건너뛰며, 그 점에 있는 모든 체크포인트를 건너뛰지 않는다.
"""

n = int(input())

checkpoints = [tuple(map(int, input().split())) for _ in range(n)]
# print('checkpoints', checkpoints)

answer = float('inf')

# 제외할 체크포인터 인덱스
for i in range(1, n-1): 
    targets = checkpoints[:i] + checkpoints[i + 1:]

    # 거리 계산
    tmp_sum = 0
    for j in range(1, len(targets)):
        prev = targets[j - 1]
        cur = targets[j]
        tmp_sum += abs(prev[0] - cur[0]) + abs(prev[1] - cur[1])

    answer = min(answer, tmp_sum)

print(answer)