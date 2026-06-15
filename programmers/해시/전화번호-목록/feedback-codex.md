# 전화번호 목록 풀이 피드백

## 문제 조건 요약

- 문제 설명은 같은 디렉토리의 이미지 파일로 확인했다.
- `phone_book`의 길이는 최대 1,000,000이고, 각 전화번호 길이는 최대 20이다.
- 어떤 전화번호가 다른 전화번호의 접두어이면 `False`, 그런 경우가 없으면 `True`를 반환해야 한다.

## 풀이가 바뀐 흐름

이 문제는 처음에는 정렬을 이용해서 풀기 시작했다.

`c5fb143` 커밋의 풀이는 `phone_book`을 정렬한 뒤, 앞에 있는 번호가 뒤에 있는 번호의 접두어인지 전부 확인하는 방식이었다.

```python
def solution(phone_book):
    len_phone_book = len(phone_book)
    phone_book.sort()

    for i in range(len_phone_book-1):
        for j in range(i+1, len_phone_book):
            v1 = phone_book[i]
            v2 = phone_book[j]

            if v2.startswith(v1):
                return False

    return True
```

정렬을 먼저 한 판단은 좋았다. 문자열을 정렬하면 접두어 관계가 있는 전화번호들이 가까이 오기 때문이다.

문제는 정렬 후에도 모든 뒤쪽 번호를 다시 비교했다는 점이다. `phone_book`의 길이가 최대 1,000,000이라서, 이중 반복문은 최악의 경우 `O(n^2)`가 되고 시간 초과가 난다.

정렬 풀이를 유지한다면 모든 쌍을 볼 필요 없이, 정렬 후 바로 옆 번호만 비교하면 된다.

```python
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True
```

## 해시 풀이로 바꾼 이유

그다음 `1b54c86` 커밋에서는 Codex 피드백을 반영해서 해시 접근으로 바꿨다.

핵심 아이디어는 모든 전화번호 쌍을 비교하지 말고, 전체 전화번호를 빠르게 조회할 수 있는 자료구조에 넣어 둔 다음, 각 전화번호의 접두어가 실제 목록에 있는지만 확인하는 것이다.

예를 들어 `"1195524421"`이 있으면 확인해야 할 접두어 후보는 아래와 같다.

```text
"1"
"11"
"119"
"1195"
...
"119552442"
```

이 중 하나가 전체 전화번호 목록 안에 있으면, 어떤 번호가 다른 번호의 접두어라는 뜻이다. 반대로 아무 접두어도 목록에 없으면 그 번호는 문제 조건을 위반하지 않는다.

이 접근은 겉으로 보면 반복문이 중첩되어 있지만, 안쪽 반복이 전화번호 개수 `n`이 아니라 전화번호 길이 `L`에 대해서만 돈다.

- 모든 쌍 비교: `O(n^2)`
- 접두어 후보 조회: 대략 `O(n * L)`

이 문제에서는 전화번호 길이 `L`이 최대 20으로 작기 때문에, 탐색 비용을 `n^2`에서 `n * L` 쪽으로 옮기는 것이 핵심이다.

## `Counter`를 거쳐 `set`으로 정리한 이유

`1b54c86` 커밋의 해시 풀이는 `Counter`를 사용했다.

```python
from collections import Counter

def solution(phone_book):
    prefix_candidates = Counter(phone_book)

    for p in phone_book:
        for i in range(1, len(p)):
            if p[0:i] in prefix_candidates:
                return False

    return True
```

이 코드는 동작한다. `Counter`도 내부적으로 딕셔너리 계열이라서 `in`으로 키 존재 여부를 확인할 수 있기 때문이다.

다만 이 문제에서 필요한 것은 "각 전화번호가 몇 번 나왔는가"가 아니라 "이 문자열이 전화번호 목록에 있는가"뿐이다. 게다가 문제 조건상 같은 전화번호는 중복해서 들어오지 않는다.

그래서 이후 피드백에서는 `Counter`보다 `set`이 더 자연스럽다고 정리했다.

```python
def solution(phone_book):
    prefix_candidates = set(phone_book)

    for p in phone_book:
        for i in range(1, len(p)):
            if p[0:i] in prefix_candidates:
                return False

    return True
```

현재 `main.py`는 이 방향으로 바뀌어 있다. `Counter`에서 `set`으로 바꾼 것은 알고리즘을 새로 바꾼 것이라기보다, 같은 해시 조회 풀이에서 문제에 더 맞는 자료구조를 선택한 것이다.

## 현재 풀이에서 좋은 점

- 전체 전화번호를 `set`에 넣어 접두어 존재 여부를 빠르게 확인한다.
- 모든 번호 쌍을 비교하지 않고, 각 번호의 접두어 후보만 확인한다.
- `range(1, len(p))`를 사용해서 자기 자신 전체 문자열은 검사하지 않는다.
- 접두어를 찾는 즉시 `False`를 반환해서 불필요한 검사를 줄인다.

## 더 다듬을 부분

`prefix_candidates`라는 이름은 조금 헷갈릴 수 있다. 실제로 담겨 있는 것은 접두어 후보가 아니라 전체 전화번호 목록이다.

아래처럼 바꾸면 변수의 역할이 더 분명하다.

```python
phone_numbers = set(phone_book)
```

또 `p[0:i]`는 맞는 표현이지만, 파이썬에서는 앞에서부터 자를 때 보통 `p[:i]`를 더 자주 쓴다.

```python
if phone[:i] in phone_numbers:
    return False
```

정리하면 개선 예시는 다음과 같다.

```python
def solution(phone_book):
    phone_numbers = set(phone_book)

    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_numbers:
                return False

    return True
```

## 추가 테스트

현재 풀이로 직접 실행한 테스트는 모두 기대값과 일치했다.

```text
["119", "97674223", "1195524421"] -> False
["123", "456", "789"] -> True
["12", "123", "1235", "567", "88"] -> False
["1"] -> True
["91125426", "97625999", "911"] -> False
["123", "124", "125"] -> True
```

특히 `["91125426", "97625999", "911"]`처럼 접두어가 입력 뒤쪽에 있는 경우도 잘 처리한다. 입력 순서에 의존하지 않고 `set` 조회로 판단하기 때문이다.

## 다음 문제에 적용할 점

해시 문제에서는 먼저 "무엇을 빠르게 찾을 것인가"를 정해야 한다.

이번 문제에서는 접두어 후보가 실제 전화번호 목록에 있는지 빠르게 찾아야 했다. 그래서 전체 전화번호를 `set`에 저장하고, 각 번호에서 만들어지는 접두어를 조회하는 방식이 자연스럽다.

또 정렬 풀이처럼 좋은 출발점을 잡았더라도, 정렬 이후에 모든 쌍을 다시 비교하면 정렬의 장점을 살리지 못한다. 정렬을 썼다면 인접한 원소만 보면 되는지까지 같이 확인하는 습관을 들이면 좋다.
