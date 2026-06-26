# 7696 반복하지 않는 수 - Codex 피드백

## 문제 조건 요약

- 여러 개의 테스트 케이스가 입력되며, `0`이 들어오면 종료한다.
- 각 테스트 케이스마다 `n`번째 반복 숫자 없는 수를 출력한다.
- `1 <= n <= 1,000,000`이므로, 입력이 여러 개일 때 같은 계산을 반복하지 않는 구조를 생각해볼 수 있다.

## 현재 풀이의 좋은 점

현재 `main.py`는 `answer`를 1씩 증가시키면서 `validate(answer)`로 각 자리 숫자의 중복 여부를 검사한다.

```python
def validate(number):
    digits = str(number)
    return len(digits) == len(set(digits))
```

이 검사는 읽기 쉽고 Pythonic하다. 숫자를 문자열로 바꾼 뒤 `set`으로 중복을 제거해서 길이를 비교하는 방식이라, 이 문제의 조건을 직접적으로 표현한다.

## 개선 포인트: 여러 입력을 한 번에 처리하기

현재 구조는 테스트 케이스마다 1부터 다시 탐색한다.

예를 들어 입력이 다음과 같다고 하자.

```text
25
10000
0
```

현재 흐름은 다음과 같다.

1. `25`번째 답을 구하기 위해 1부터 27까지 탐색한다.
2. `10000`번째 답을 구하기 위해 다시 1부터 26057까지 탐색한다.

하지만 `10000`번째 답을 구하는 과정 안에는 이미 `25`번째 답도 포함되어 있다. 따라서 입력을 먼저 모두 모아두고, 그중 가장 큰 값까지만 한 번 계산해두면 중복 탐색을 줄일 수 있다.

핵심 아이디어는 다음과 같다.

```python
queries = [25, 10000]
max_n = max(queries)
```

`max_n`이 `10000`이면 반복 숫자 없는 수를 `10000`개까지만 한 번 만든다. 이후 각 입력에 대해서는 미리 만든 리스트에서 바로 꺼내면 된다.

```python
answers[n - 1]
```

여기서 `n - 1`을 쓰는 이유는 문제의 순서는 1번째부터 세지만, Python 리스트 인덱스는 0부터 시작하기 때문이다.

## 개선 예시

아래 코드는 현재 풀이의 `validate()` 흐름은 유지하면서, 여러 테스트 케이스를 한 번에 처리하도록 바꾼 예시다.

```python
def validate(number):
    digits = str(number)
    return len(digits) == len(set(digits))


queries = []
while True:
    n = int(input())
    if n == 0:
        break
    queries.append(n)

max_n = max(queries)

answers = []
number = 1
while len(answers) < max_n:
    if validate(number):
        answers.append(number)
    number += 1

for n in queries:
    print(answers[n - 1])
```

## 주의할 점

위 개선 예시는 입력이 최소 한 개 이상 있다는 전제에서 자연스럽게 동작한다. 만약 `0`만 입력되는 경우까지 방어적으로 처리하고 싶다면 `max(queries)`를 호출하기 전에 `queries`가 비어 있는지 확인하면 된다.

```python
if not queries:
    exit()
```

## 다음 문제에 적용할 교훈

여러 테스트 케이스가 있고 각 테스트가 같은 순서열의 일부를 묻는다면, 매번 처음부터 계산하지 말고 가장 큰 요청까지만 한 번 계산해두는 방식을 먼저 떠올려보자.
