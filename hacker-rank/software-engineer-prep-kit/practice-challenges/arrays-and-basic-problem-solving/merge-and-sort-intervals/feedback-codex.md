# Merge and Sort Intervals 피드백

## 문제 조건 요약

- 입력은 `N`, 각 interval의 길이 `2`, 이후 `N`개의 `startTime endTime`으로 주어진다.
- 각 구간은 `[startTime, endTime]` 형태이며, 문제 조건상 `startTime <= endTime`이다.
- 결과는 시작 시간이 증가하는 순서로 병합된 구간들을 출력한다.

PDF는 텍스트 추출이 되지 않아 이미지 렌더링으로 입력 형식과 제한 조건을 확인했다.

## 잘한 점

- 시작 시간 기준으로 정렬한 뒤, 마지막으로 병합된 구간과 현재 구간만 비교하는 방향이 좋다.
- `answer[-1]`을 기준으로 병합 여부를 판단하므로 별도의 복잡한 자료구조가 필요 없다.
- 빈 입력에 대해 `[]`를 반환하는 처리가 있어 `intervals[0]` 접근 오류를 피했다.

## 개선 과정

### 1. 각 interval 내부 정렬 제거

처음 풀이에는 다음과 같은 처리가 있었다.

```python
for i in intervals:
    i.sort()
```

하지만 이 문제에서 각 interval은 `[startTime, endTime]`이라는 의미를 가진다. 문제 조건상 `startTime <= endTime`이 보장되므로 내부 정렬은 필요 없다.

더 적절한 처리는 구간 전체를 시작 시간 기준으로만 정렬하는 것이다.

```python
intervals.sort(key=lambda x: x[0])
```

이렇게 하면 입력 데이터의 의미를 유지하면서도 병합에 필요한 순서를 만들 수 있다.

### 2. 인덱스 반복문을 값 중심 반복문으로 변경

초기 형태는 인덱스를 직접 사용했다.

```python
for i in range(1, len(intervals)):
    cur = intervals[i]
    cur_start = cur[0]
    cur_end = cur[1]
```

현재처럼 값을 바로 꺼내면 현재 구간을 다루는 의도가 더 분명해진다.

```python
for cur_start, cur_end in intervals[1:]:
```

이 정도의 unpacking은 코딩 테스트에서도 읽기 쉽고 실수 가능성이 낮다.

### 3. 병합 구간 갱신 방식 단순화

겹치는 경우에는 마지막 병합 구간의 끝값만 늘리면 된다.

```python
if cur_start <= target_end:
    answer[-1][1] = max(target_end, cur_end)
```

새 구간을 통째로 다시 만들 필요 없이 끝값만 갱신하므로 코드가 간단해졌다.

## 남은 정리 포인트

- 주석 처리된 디버그 `print`는 제출 전 제거하는 편이 좋다.
- `intervals_columns`는 입력 소비 목적만 있으므로 `_ = int(input().strip())`처럼 받아도 된다.
- `target = answer[-1]`, `_, target_end = target`도 괜찮지만, 더 짧게는 `target_end = answer[-1][1]`로 충분하다.
- 빈 결과일 때 현재 출력부는 빈 줄 하나를 출력할 수 있다. 채점에 문제 없을 가능성이 높지만, 더 엄밀하게 하려면 `result`가 있을 때만 출력할 수 있다.

## 개선 예시

아래는 현재 풀이 흐름을 유지하면서 제출용으로 조금 더 정리한 예시다.

```python
def mergeHighDefinitionIntervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    answer = [intervals[0]]
    for cur_start, cur_end in intervals[1:]:
        target_end = answer[-1][1]

        if cur_start <= target_end:
            answer[-1][1] = max(target_end, cur_end)
        else:
            answer.append([cur_start, cur_end])

    return answer
```

## 복잡도

- 시간 복잡도: `O(N log N)`
  - 시작 시간 기준 정렬이 가장 큰 비용이다.
- 공간 복잡도: `O(N)`
  - 최악의 경우 어떤 구간도 병합되지 않으면 결과 배열에 모든 구간이 들어간다.

## 다음 문제에 적용할 교훈

문제 조건이 보장하는 값은 다시 고치려 하지 말고, 풀이에 필요한 순서나 상태만 직접 관리하자. 이번 문제에서는 각 구간 내부를 정렬하는 것이 아니라, 구간 목록을 시작 시간 기준으로 정렬하는 것이 핵심이었다.
