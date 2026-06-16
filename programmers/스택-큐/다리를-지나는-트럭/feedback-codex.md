# 다리를 지나는 트럭 풀이 피드백

## 문제 조건 요약

- 문제 설명은 같은 디렉토리의 이미지 파일로 확인했다.
- 다리에는 최대 `bridge_length`대의 트럭이 올라갈 수 있다.
- 다리 위 트럭들의 무게 합은 `weight` 이하이어야 한다.
- 모든 트럭이 주어진 순서대로 다리를 건너는 데 걸리는 최소 시간을 반환해야 한다.
- `bridge_length`, `weight`, `truck_weights`의 길이는 각각 최대 10,000이다.

## 현재 풀이 요약

현재 풀이는 남은 트럭을 `remain_trucks`, 다리 위 트럭을 `bridge_q`로 관리한다.

```python
remain_trucks = deque(truck_weights)
bridge_q = deque()
```

다리 위 트럭은 `(무게, 진행도)` 형태로 저장하고, 매초마다 모든 트럭의 진행도를 1씩 증가시킨다.

```python
for i, truck in enumerate(bridge_q):
    weight, process = truck
    bridge_q[i] = (weight, process + 1)
```

맨 앞 트럭의 진행도가 `bridge_length`를 넘으면 다리를 지난 것으로 보고 제거한다.

```python
if bridge_q and bridge_q[0][1] > bridge_length:
    bridge_q.popleft()
```

이후 다리 위 트럭 무게 합과 다음 트럭 무게를 비교해서, 올라갈 수 있으면 새 트럭을 다리에 올린다.

```python
if remain_trucks and sum([w for w, _ in bridge_q]) + remain_trucks[0] <= weight_limit:
    bridge_q.append((remain_trucks[0], 1))
    remain_trucks.popleft()
```

## 잘한 점

- 남은 트럭과 다리 위 트럭을 `deque`로 나눠 관리한 점은 문제의 큐 성격과 잘 맞는다.
- 트럭이 들어온 순서대로 다리를 건너야 한다는 조건을 잘 지키고 있다.
- 다리 위 첫 번째 트럭부터 빠지는 구조를 `popleft()`로 표현한 점도 좋다.
- 예제와 추가 테스트에서 기대한 결과와 일치했다.

직접 확인한 테스트:

```text
bridge_length=2, weight=10, truck_weights=[7,4,5,6] -> 8
bridge_length=100, weight=100, truck_weights=[10] -> 101
bridge_length=100, weight=100, truck_weights=[10]*10 -> 110
bridge_length=1, weight=10, truck_weights=[10] -> 2
bridge_length=1, weight=10, truck_weights=[5,5,5] -> 4
bridge_length=2, weight=10, truck_weights=[5,5,5] -> 5
bridge_length=3, weight=10, truck_weights=[10,10,10] -> 10
```

## 아쉬운 점

### 1. `deque`를 쓰면서 인덱스 수정이 많다

현재 코드는 매초 다리 위 모든 트럭을 순회하면서 `bridge_q[i]`를 수정한다.

```python
bridge_q[i] = (weight, process + 1)
```

`deque`는 양쪽 끝에서 넣고 빼는 작업에 강한 자료구조다.

```python
append()
popleft()
```

이런 작업은 빠르다. 하지만 중간 인덱스 접근이나 수정은 리스트처럼 빠른 용도가 아니다. `deque`는 내부적으로 여러 블록이 연결된 구조에 가까워서, 중간 위치를 자주 찾고 수정하는 방식은 장점을 살리기 어렵다.

정리하면 다음과 같다.

```text
인덱스로 자주 접근/수정한다 -> list가 자연스럽다
앞/뒤에서 자주 넣고 뺀다 -> deque가 자연스럽다
```

현재 풀이는 `deque`를 쓰고 있지만, 실제로는 매초 전체 원소를 인덱스로 수정하고 있어서 큐의 장점을 충분히 활용하지 못한다.

### 2. 매번 다리 위 무게 합을 다시 계산한다

현재 코드는 새 트럭이 올라갈 수 있는지 확인할 때마다 다리 위 모든 트럭 무게를 다시 더한다.

```python
sum([w for w, _ in bridge_q])
```

이 표현은 두 가지 비용이 있다.

- 다리 위 트럭을 매번 전부 순회한다.
- 리스트 컴프리헨션 때문에 중간 리스트도 새로 만든다.

최소한 아래처럼 쓰면 중간 리스트는 만들지 않는다.

```python
sum(w for w, _ in bridge_q)
```

하지만 더 좋은 방식은 `current_weight` 변수를 따로 유지하는 것이다. 트럭이 다리에 올라갈 때 더하고, 다리에서 빠질 때 빼면 매번 전체 합을 다시 계산할 필요가 없다.

## 개선 방향

이 문제는 다리 자체를 길이 `bridge_length`짜리 큐로 보면 더 단순해진다.

매초마다 다음 작업을 한다.

```text
1. 다리 맨 앞 칸을 popleft()로 뺀다.
2. 빠진 트럭 무게만큼 current_weight에서 뺀다.
3. 다음 트럭이 올라갈 수 있으면 append(트럭 무게)한다.
4. 못 올라가면 append(0)으로 빈 칸을 넣는다.
```

이렇게 하면 트럭마다 진행도를 따로 저장하지 않아도 된다. 다리 큐에서 한 칸씩 앞으로 이동하는 것 자체가 시간이 흐르는 것을 의미한다.

## 개선 예시

```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current_weight = 0

    while trucks:
        time += 1
        current_weight -= bridge.popleft()

        if current_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

    return time + bridge_length
```

`return time + bridge_length`를 하는 이유는 마지막 트럭이 다리에 올라간 뒤에도 다리를 완전히 빠져나가기까지 `bridge_length`초가 더 필요하기 때문이다.

## `list`와 `deque` 선택 기준

앞에서 하나 빼고 뒤에 하나 넣는 방식은 `deque`에서는 빠르지만, `list`에서는 느리다.

```python
bridge.pop(0)
```

리스트에서 `pop(0)`을 하면 맨 앞 원소를 제거한 뒤 뒤의 원소들을 전부 한 칸씩 앞으로 당겨야 하므로 `O(n)`이다.

반면 `deque`는 아래 연산이 모두 빠르다.

```python
bridge.popleft()
bridge.append(truck)
```

그래서 이 문제처럼 매초 앞에서 하나 빠지고 뒤에 하나 들어오는 구조는 `deque`가 잘 맞는다.

## 다음 문제에 적용할 점

큐 문제에서는 단순히 `deque`를 쓰는 것보다, 실제 연산이 `popleft()`와 `append()` 중심인지 확인하는 것이 중요하다.

이번 문제의 핵심은 트럭마다 진행도를 따로 올리는 것이 아니라, 다리를 고정 길이 큐로 보고 시간이 흐를 때마다 한 칸씩 밀어내는 것이다.
