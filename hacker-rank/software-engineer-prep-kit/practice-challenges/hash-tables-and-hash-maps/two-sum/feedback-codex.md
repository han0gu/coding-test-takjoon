# Two Sum 피드백

## 문제 조건 요약

- PDF는 텍스트 추출이 되지 않아 이미지 렌더링으로 조건을 확인했다.
- `taskDurations[i] + taskDurations[j] == slotLength`인 두 인덱스 `i`, `j`를 반환해야 한다.
- 인덱스는 `0 <= i < j < n`이어야 하며, 유효한 쌍이 여러 개면 아무 쌍이나 출력해도 된다.
- 유효한 쌍이 없으면 `[-1, -1]`을 반환한다.

## 현재 코드 판단

현재 풀이의 핵심 흐름은 다음과 같다.

1. `Counter(taskDurations)`로 각 duration 값의 존재 여부를 확인한다.
2. 각 인덱스 `i`에서 필요한 값 `slotLength - taskDurations[i]`를 계산한다.
3. 필요한 값이 존재하면 `i + 1`부터 다시 순회하면서 실제 인덱스 `j`를 찾는다.
4. 찾으면 `[i, j]`를 반환하고, 끝까지 없으면 `[-1, -1]`을 반환한다.

PDF 조건 안에서는 이 로직의 명확한 오답 반례를 찾기 어렵다. 특히 `j`를 항상 `i + 1`부터 찾기 때문에 같은 인덱스를 두 번 쓰는 문제도 피하고 있다.

다만 HackerRank 제출 결과가 일부 Wrong Answer라면, 현재 파일만으로는 다음 가능성을 먼저 의심해볼 수 있다.

- 실제 제출한 코드가 현재 `main.py`와 다른 경우
- HackerRank 제공 스텁이나 함수 시그니처가 제출 코드와 어긋난 경우
- 문제 설명에는 없는 입력이 채점 데이터에 포함된 경우

예를 들어 문제 설명은 `1 <= taskDurations[i]`라고 되어 있지만, 만약 `0`이 들어온다면 현재 방어 코드가 영향을 줄 수 있다.

```python
taskDurations = [0, 1]
slotLength = 1
```

이 경우 이론상 정답은 `[0, 1]`이지만, 현재 코드는 `slotLength < 2` 조건 때문에 `[-1, -1]`을 반환한다. 다만 이 입력은 PDF의 제한 조건 밖이다.

## `Counter` 사용에 대한 피드백

현재 코드는 `Counter`를 값의 개수 확인 용도로 쓰고 있다. 그 자체가 틀린 사용은 아니다.

다만 이 문제는 `True/False`가 아니라 인덱스를 반환해야 한다. 그래서 `Counter`로 값 존재 여부를 확인한 뒤, 실제 인덱스를 찾기 위해 다시 반복문을 도는 구조가 된다.

`Counter`를 개수 확인 중심으로 쓰면 보통 이런 형태가 된다.

```python
from collections import Counter

def has_pair(taskDurations, slotLength):
    counts = Counter(taskDurations)

    for x in counts:
        y = slotLength - x

        if y not in counts:
            continue

        if x != y:
            return True

        if counts[x] >= 2:
            return True

    return False
```

핵심은 `x == y`일 때만 같은 값이 최소 2개 필요한지 확인하면 된다는 점이다.

하지만 이 코드는 인덱스를 반환하지 않는다. 인덱스를 반환하려면 결국 추가 처리가 필요하다.

## Hash Map 카테고리에 더 잘 맞는 풀이 방향

이 문제는 `"hash tables and hash maps"` 카테고리이므로, 값의 존재 여부뿐 아니라 인덱스까지 딕셔너리에 저장하는 방식이 더 자연스럽다.

추천하는 구조는 `이미 본 값 -> 그 값의 인덱스`를 저장하면서 한 번만 순회하는 방식이다.

```python
def findTaskPairForSlot(taskDurations, slotLength):
    seen = {}

    for i, duration in enumerate(taskDurations):
        need = slotLength - duration

        if need in seen:
            return [seen[need], i]

        seen[duration] = i

    return [-1, -1]
```

이 방식의 장점은 다음과 같다.

- 필요한 값이 이전에 나왔는지 `O(1)` 평균 시간에 확인할 수 있다.
- 값을 찾는 순간 바로 이전 인덱스도 함께 얻을 수 있다.
- 별도의 중첩 반복문이 없어 흐름이 단순하다.
- `i < j` 조건도 자연스럽게 만족한다. 현재 인덱스 `i`를 보기 전에 저장된 값은 항상 앞쪽 인덱스이기 때문이다.

## 복잡도 비교

| 방식 | 시간 복잡도 | 공간 복잡도 | 특징 |
| --- | --- | --- | --- |
| 현재 `Counter` + 내부 반복문 | 최악 `O(n^2)` | `O(n)` | 존재 확인은 빠르지만 인덱스를 다시 찾는다. |
| `dict[value] = index` | 평균 `O(n)` | `O(n)` | 값 확인과 인덱스 조회를 한 번에 처리한다. |

문제 제한이 `n <= 1000`이라면 현재 방식도 시간 초과가 나기 쉬운 크기는 아니다. 그래도 카테고리 의도와 코드 단순성까지 고려하면 `dict[value] = index` 방식이 더 좋은 풀이로 볼 수 있다.

## 다음에 적용할 교훈

해시맵 문제에서는 단순히 값이 있는지만 확인할지, 값과 함께 어떤 정보까지 바로 꺼내야 하는지를 먼저 정리하는 것이 좋다.

이 문제에서는 반환값이 인덱스이므로 `duration -> index` 형태의 딕셔너리를 쓰는 편이 가장 직접적이다.
