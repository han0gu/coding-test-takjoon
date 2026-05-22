"""
마라톤 코스는 N (3 ≤ N ≤ 100000) 개의 체크포인트

-1000 ≤ x, y ≤ 1000

체크 포인트의 좌표는 겹칠 수도 있다
그 번호의 체크포인트만 건너뛰며, 그 점에 있는 모든 체크포인트를 건너뛰지 않는다.
"""

n = int(input())

checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

def get_distance(p1: tuple, p2: tuple) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# 모두 방문할 경우 거리 계산
no_exclude = 0
for i in range(1, n):
    no_exclude += get_distance(checkpoints[i - 1], checkpoints[i])

# 제외할 체크포인트 인덱스
answer = no_exclude
for i in range(1, n-1):
    exclude = get_distance(checkpoints[i-1], checkpoints[i]) + get_distance(checkpoints[i], checkpoints[i+1])
    include = get_distance(checkpoints[i-1], checkpoints[i+1])

    answer = min(answer, no_exclude - exclude + include)

print(answer)
