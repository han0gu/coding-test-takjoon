# 10655 - 마라톤 1 풀이 피드백

## 문제 조건 요약

- 체크포인트는 `N`개이며, `3 <= N <= 100000`이다.
- 1번과 N번 체크포인트는 건너뛸 수 없고, 중간 체크포인트 중 정확히 1개를 건너뛰어야 한다.
- 두 점 사이의 거리는 맨해튼 거리 `|x1 - x2| + |y1 - y2|`로 계산한다.
- PDF는 텍스트 추출이 되지 않아 이미지 렌더링으로 조건을 확인했다.

## 현재 풀이 요약

현재 `main.py`는 중간 체크포인트를 하나씩 제외해 보고, 제외된 경로의 전체 거리를 다시 계산한다.

```python
for i in range(1, n-1):
    targets = checkpoints[:i] + checkpoints[i + 1:]

    tmp_sum = 0
    for j in range(1, len(targets)):
        prev = targets[j - 1]
        cur = targets[j]
        tmp_sum += abs(prev[0] - cur[0]) + abs(prev[1] - cur[1])

    answer = min(answer, tmp_sum)
```

제출 통과 기준으로는 풀이 방향을 잘 잡았다. "하나를 빼고 남은 경로의 거리 합을 구한다"는 접근은 문제 요구사항을 그대로 코드로 옮긴 형태라 이해하기 쉽다.

## 잘한 점

1. 건너뛸 수 있는 체크포인트 범위를 `range(1, n-1)`로 잡아 1번과 N번 체크포인트를 제외하지 않도록 처리했다.
2. 맨해튼 거리 계산식을 직접 풀어 써서 문제 조건과 코드가 잘 대응된다.
3. 좌표를 `tuple`로 저장해 각 체크포인트를 하나의 값처럼 다룬 점도 적절하다.

## 개선할 점

가장 큰 개선점은 시간 복잡도다.

현재 코드는 중간 체크포인트마다 다음 두 일을 반복한다.

1. `checkpoints[:i] + checkpoints[i + 1:]`로 새 리스트를 만든다.
2. 새 리스트 전체를 돌면서 거리를 다시 계산한다.

그래서 전체 시간 복잡도는 `O(N^2)`이다. 문제 제한이 `N <= 100000`이므로, 제한 전체를 기준으로 보면 이 방식은 너무 크다.

이 문제는 전체 거리를 먼저 구한 뒤, 특정 체크포인트를 건너뛸 때 바뀌는 구간만 다시 계산하면 된다.

예를 들어 `i`번 체크포인트를 건너뛴다면 바뀌는 부분은 아래 세 점뿐이다.

```text
기존: i-1 -> i -> i+1
변경: i-1 -> i+1
```

따라서 매번 전체 경로를 다시 계산할 필요가 없다.

## 개선 예시

아래 코드는 현재 풀이의 아이디어를 유지하면서, 전체 거리를 한 번만 구하고 바뀌는 부분만 반영하는 방식이다.

```python
def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


n = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n - 1):
    total += dist(checkpoints[i], checkpoints[i + 1])

answer = total

for i in range(1, n - 1):
    before = dist(checkpoints[i - 1], checkpoints[i]) + dist(checkpoints[i], checkpoints[i + 1])
    after = dist(checkpoints[i - 1], checkpoints[i + 1])
    answer = min(answer, total - before + after)

print(answer)
```

## 복잡도 비교

| 방식 | 시간 복잡도 | 설명 |
| --- | --- | --- |
| 현재 풀이 | `O(N^2)` | 체크포인트를 하나 뺄 때마다 전체 경로를 다시 계산 |
| 개선 풀이 | `O(N)` | 전체 거리를 한 번 구하고, 각 체크포인트마다 바뀌는 세 점만 확인 |

공간 복잡도는 두 방식 모두 좌표 저장 때문에 기본적으로 `O(N)`이다. 다만 현재 풀이는 반복 중 새 리스트를 계속 만들기 때문에 실제 실행 비용이 더 커진다.

## 다음 문제에 적용할 교훈

"하나를 제거하고 전체를 다시 계산하는 풀이"가 떠오르면, 먼저 전체값을 구한 뒤 제거로 인해 바뀌는 부분만 갱신할 수 있는지 확인해보자.

이 문제에서는 전체 경로 중 바뀌는 구간이 `i-1`, `i`, `i+1` 세 체크포인트 주변뿐이었기 때문에 `O(N^2)` 풀이를 `O(N)`으로 줄일 수 있었다.
