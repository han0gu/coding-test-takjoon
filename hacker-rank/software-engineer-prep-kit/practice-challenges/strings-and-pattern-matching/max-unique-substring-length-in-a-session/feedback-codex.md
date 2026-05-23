# Max Unique Substring Length in a Session 피드백

## 문제 조건 요약

- PDF는 텍스트 추출이 되지 않아 이미지 렌더링으로 조건을 확인했다.
- 입력 문자열은 소문자와 `*`로 구성되고, `*`는 session 구분자다.
- 각 session 안에서 중복 문자가 없는 substring의 최대 길이를 구해야 한다.
- 입력이 비어 있거나 `*`만 있으면 `0`을 출력한다.

## 기존 풀이의 핵심 문제

기존 코드는 각 session을 앞에서부터 보다가 이미 나온 문자를 만나면 바로 `break`했다.

```python
visited = []

for c in string:
    if c in visited:
        break
    visited.append(c)
```

이 방식은 session의 맨 앞에서 시작하는 prefix만 확인한다. 하지만 문제에서 요구하는 것은 prefix가 아니라 substring이므로, 시작 위치가 중간일 수도 있다.

예를 들어 다음 입력을 보자.

```text
aab
```

기존 코드는 첫 번째 `a` 다음 두 번째 `a`를 만나면 멈추기 때문에 길이 `1`을 반환한다. 하지만 실제로는 substring `"ab"`가 중복 없는 문자열이고 길이는 `2`다.

따라서 PDF 문구 기준 기대값은 `2`가 되어야 한다.

## 수정 방향

각 session마다 sliding window를 사용한다.

- `start`: 현재 중복 없는 구간의 시작 위치
- `end`: 현재 보고 있는 문자 위치
- `visited`: 현재 window 안에 들어 있는 문자 집합

새 문자가 이미 window 안에 있으면, 그 문자가 없어질 때까지 왼쪽에서 문자를 제거하면서 `start`를 오른쪽으로 이동한다. 그 다음 새 문자를 추가하고, 현재 window 길이를 답에 반영한다.

## 수정 코드의 핵심

```python
for string in sessionString.split('*'):
    start = 0
    visited = set()

    for end, c in enumerate(string):
        while c in visited:
            visited.remove(string[start])
            start += 1

        visited.add(c)
        answer = max(answer, end - start + 1)
```

이제 `aab`처럼 앞부분에서 중복이 생겨도, 뒤쪽 substring `"ab"`를 계속 검사할 수 있다.

## 복잡도

- 시간 복잡도: `O(n)`
- 공간 복잡도: `O(1)` 또는 `O(k)`

여기서 `n`은 전체 문자열 길이이고, `k`는 한 window 안에 들어갈 수 있는 문자 종류 수다. 문제 조건상 문자는 소문자이므로 실제 문자 종류 수는 최대 26개다.

## 다음에 적용할 교훈

문제에서 substring의 최댓값을 묻는다면, 맨 앞에서 시작하는 경우만 보면 부족할 수 있다. 중간에서 시작하는 후보까지 봐야 하므로 sliding window를 먼저 떠올리는 것이 좋다.
