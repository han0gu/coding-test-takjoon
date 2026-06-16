# 주식가격 풀이 피드백

## 문제 조건 요약

- 문제 설명은 같은 디렉토리의 이미지 파일로 확인했다.
- 각 시점의 주식 가격이 몇 초 동안 떨어지지 않는지 구해야 한다.
- 가격이 떨어지는 바로 그 순간도 경과 시간에 포함한다.
- `prices`의 길이는 2 이상 100,000 이하이다.

## 처음 풀이 요약

처음 `main.py`는 완전탐색으로 작성되어 있었다.

```python
def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        cnt = 0

        for j in range(i+1, len(prices)):
            cnt += 1

            if prices[i] > prices[j]:
                break

        answer.append(cnt)

    answer.append(0)
    return answer
```

## 처음 풀이에서 좋은 점

- 문제 설명과 거의 같은 흐름이라 이해하기 쉽다.
- 각 시점 `i`마다 오른쪽을 보며 처음 가격이 떨어지는 순간까지 센다.
- 떨어지는 시점도 시간에 포함하도록 `cnt += 1`을 먼저 하는 구조가 정확하다.
- 예제와 추가 테스트에서 기대값과 일치했다.

직접 확인한 테스트:

```text
prices=[1, 2, 3, 2, 3] -> [4, 3, 1, 1, 0]
prices=[5, 1] -> [1, 0]
prices=[3, 3, 1] -> [2, 1, 0]
prices=[1, 2, 3, 4] -> [3, 2, 1, 0]
prices=[4, 3, 2, 1] -> [1, 1, 1, 0]
```

## 처음 풀이의 아쉬운 점

완전탐색은 직관적이지만 최악의 경우 `O(n^2)`이다.

예를 들어 가격이 계속 오르거나 같으면, 각 인덱스마다 거의 끝까지 확인해야 한다.

```python
prices = [1, 2, 3, 4, 5, ...]
```

이 문제는 `prices` 길이가 최대 100,000이므로, 최악의 경우 완전탐색은 시간 초과 위험이 크다.

## 현재 풀이 요약

현재 `main.py`는 위 피드백을 반영해 단조 스택으로 작성되어 있다.

```python
def solution(prices):
    answer = [0] * len(prices)
    remain_indices = []

    for i, p in enumerate(prices):
        while remain_indices and prices[remain_indices[-1]] > p:
            top = remain_indices.pop()
            answer[top] = i - top

        remain_indices.append(i)

    for i in remain_indices:
        answer[i] = len(prices) - 1 - i

    return answer
```

- 각 인덱스는 스택에 한 번 들어가고 최대 한 번만 빠진다.
- 따라서 전체 시간 복잡도는 `O(n)`이다.
- 결과 배열과 스택을 사용하므로 공간 복잡도는 `O(n)`이다.

## 스택 풀이의 핵심 아이디어

이 문제를 스택으로 푸는 핵심은 다음 관찰이다.

```text
아직 답이 확정되지 않은 과거 시점들을 스택에 저장해두고,
현재 가격이 오면 그중 가격이 떨어진 시점들의 답을 즉시 확정한다.
```

즉 스택에는 가격이 아니라 인덱스를 저장한다.

```text
stack = 아직 가격이 떨어진 시점을 찾지 못한 인덱스들
```

현재 가격이 스택 맨 위 인덱스의 가격보다 낮으면, 그 인덱스는 지금 가격이 처음 떨어진 것이다. 그러면 스택에서 꺼내고 답을 채운다.

이런 유형은 단조 스택, 또는 monotonic stack이라고 부른다. 단순히 스택 문법을 아는 것만으로 바로 떠올리기 쉽지는 않고, "현재 값이 과거 값들의 답을 확정할 수 있는가?"라는 관찰이 필요하다.

## 스택 풀이 예시

```python
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            prev_i = stack.pop()
            answer[prev_i] = i - prev_i

        stack.append(i)

    while stack:
        prev_i = stack.pop()
        answer[prev_i] = n - 1 - prev_i

    return answer
```

## 주요 코드 설명

```python
while stack and prices[stack[-1]] > price:
```

스택 맨 위 인덱스의 가격이 현재 가격보다 크면, 그 인덱스는 현재 시점에서 가격이 떨어진 것이다.

```python
prev_i = stack.pop()
answer[prev_i] = i - prev_i
```

`prev_i` 시점부터 현재 시점 `i`까지 걸린 시간을 저장한다. 이 값은 무조건 1이 아니다.

예를 들어:

```python
prices = [5, 6, 7, 4]
```

마지막 가격 `4`를 볼 때, 스택에는 `[0, 1, 2]`가 남아 있을 수 있다. 이때 현재 가격 `4` 때문에 `7`, `6`, `5`가 모두 떨어진 것으로 확정된다.

```text
인덱스 2의 가격 7 -> 1초 만에 떨어짐
인덱스 1의 가격 6 -> 2초 만에 떨어짐
인덱스 0의 가격 5 -> 3초 만에 떨어짐
```

그래서 `i - prev_i`는 `1`, `2`, `3`처럼 달라질 수 있다.

마지막 부분은 끝까지 가격이 떨어지지 않은 인덱스들을 처리한다.

```python
while stack:
    prev_i = stack.pop()
    answer[prev_i] = n - 1 - prev_i
```

`n - 1`은 마지막 인덱스다. 따라서 `n - 1 - prev_i`는 `prev_i` 시점부터 마지막 시점까지 버틴 시간이다.

예를 들어 `prices = [1, 2, 3, 2, 3]`에서 앞의 반복이 끝난 뒤에는 대략 다음 상태가 된다.

```python
answer = [0, 0, 1, 0, 0]
stack = [0, 1, 3, 4]
```

스택에 남은 인덱스들은 끝까지 자기보다 낮은 가격을 만나지 못한 시점들이다. 그래서 마지막 인덱스까지의 거리로 답을 채운다.

```text
인덱스 4 -> 4 - 4 = 0
인덱스 3 -> 4 - 3 = 1
인덱스 1 -> 4 - 1 = 3
인덱스 0 -> 4 - 0 = 4
```

최종 답은 다음과 같다.

```python
[4, 3, 1, 1, 0]
```

## 다음 문제에 적용할 점

완전탐색으로 먼저 정확한 의미를 잡는 것은 좋다. 다만 입력 크기가 크고, 각 원소에 대해 "오른쪽에서 처음 조건을 깨는 값"을 찾아야 한다면 단조 스택을 의심해볼 수 있다.

신호는 다음과 같다.

```text
다음 더 작은 값 찾기
다음 더 큰 값 찾기
오른쪽에서 처음으로 조건을 깨는 값 찾기
현재 값이 과거 인덱스들의 답을 확정하는 구조
```

이번 문제는 "현재 가격이 과거 가격들의 하락 시점을 확정할 수 있다"는 관찰이 스택 풀이의 출발점이다.
