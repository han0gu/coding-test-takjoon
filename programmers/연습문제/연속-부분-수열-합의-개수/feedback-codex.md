# 연속 부분 수열 합의 개수 피드백

## 문제 조건 요약

- 원형 수열 `elements`가 주어진다.
- 원형 수열에서 만들 수 있는 연속 부분 수열의 합을 모두 구한다.
- 서로 다른 합의 개수를 반환해야 한다.
- `elements`의 길이는 3 이상 1,000 이하이다.

## 현재 풀이의 좋은 점

현재 풀이는 원형 수열을 직접 circular queue로 구현하지 않고, 배열을 두 번 이어 붙여서 처리한다.

```python
new_elements = elements * 2
```

이 접근은 좋다. 원형 수열에서 끝과 처음이 이어지는 구간도, 배열을 두 번 이어 붙이면 일반적인 연속 구간처럼 다룰 수 있다.

예를 들어 `elements = [7, 9, 1, 1, 4]`라면:

```python
new_elements = [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
```

이렇게 만들어두면 마지막 원소 `4`에서 시작해서 처음 원소 `7`로 이어지는 구간도 슬라이싱으로 표현할 수 있다.

또한 길이 `1`부터 `n`까지 모든 연속 부분 수열을 확인하는 방향도 문제 요구사항과 맞다.

```python
for i in range(1, n + 1):
    for j in range(n):
```

각 길이마다 시작 위치는 원래 수열의 인덱스 `0`부터 `n - 1`까지만 보면 된다. 이 점도 잘 잡았다.

## 아쉬운 점

현재 코드는 구간 합을 구할 때 매번 슬라이싱과 `sum()`을 사용한다.

```python
answer.append(sum(new_elements[j:j+i]))
```

이 코드는 이해하기 쉽지만, 성능상 비용이 크다.

`new_elements[j:j+i]`는 매번 새 리스트를 만들고, `sum()`은 그 리스트를 다시 순회한다. 바깥 반복문이 이미 모든 길이와 시작점을 확인하므로 `O(n^2)`번 실행되는데, 각 `sum()`이 최대 `O(n)`까지 걸릴 수 있다.

따라서 전체 시간 복잡도는 대략 `O(n^3)`에 가까워진다.

`n <= 1000`이라 현재 코드도 로컬에서는 동작할 수 있지만, 채점 환경에서는 불안정할 수 있다.

## 개선 방향 1: 처음부터 `set` 사용하기

현재는 리스트에 모든 합을 담은 뒤 마지막에 `set`으로 바꾼다.

```python
answer = []
...
return len(set(answer))
```

이 문제는 중복을 제거한 합의 개수만 필요하므로 처음부터 `set`을 쓰는 편이 자연스럽다.

```python
answer = set()
answer.add(total)
```

이렇게 하면 중복된 합을 여러 번 리스트에 저장하지 않아도 된다.

## 개선 방향 2: 슬라이딩 윈도우로 구간 합 갱신하기

같은 길이의 구간을 한 칸씩 옮겨가며 확인할 때는 매번 합을 다시 계산할 필요가 없다.

예를 들어 길이가 `length`인 구간의 합을 알고 있다면, 시작점을 한 칸 오른쪽으로 옮길 때:

1. 이전 구간의 맨 앞 값을 뺀다.
2. 새로 들어오는 맨 뒤 값을 더한다.

```python
acc += new_elements[start + length - 1]
acc -= new_elements[start - 1]
```

이렇게 하면 각 구간 합을 `O(1)`에 갱신할 수 있다.

흐름은 다음과 같다.

```python
for length in range(1, n + 1):
    acc = sum(new_elements[:length])
    answer.add(acc)

    for start in range(1, n):
        acc += new_elements[start + length - 1]
        acc -= new_elements[start - 1]
        answer.add(acc)
```

이 방식은 길이와 시작점을 모두 확인하므로 전체 탐색 횟수는 여전히 `O(n^2)`이다. 하지만 각 구간 합을 다시 계산하지 않기 때문에 전체 시간 복잡도는 `O(n^2)`로 줄어든다.

## 정리

현재 풀이의 핵심 아이디어는 맞다.

- circular queue를 직접 구현하지 않고 `elements * 2`로 원형을 선형화한 점이 좋다.
- 모든 길이와 시작점을 확인하는 완전탐색 방향도 문제 조건에 맞다.

다만 성능을 안정적으로 만들려면 다음 두 가지를 개선하는 것이 좋다.

1. `answer`는 처음부터 `set`으로 관리한다.
2. `sum(new_elements[j:j+i])` 대신 슬라이딩 윈도우로 구간 합을 갱신한다.

이 문제는 circular queue 구현 문제가 아니라, 원형 수열을 어떻게 선형 배열처럼 다룰지와 구간 합을 얼마나 효율적으로 구할지가 핵심이다.

## 개선 후 추가 피드백

개선한 풀이는 기존 피드백의 핵심을 잘 반영했다.

```python
answer = set(elements)
```

로 길이 1짜리 부분 수열의 합을 먼저 넣고, 길이 2부터는 슬라이딩 윈도우로 합을 갱신한다.

```python
tmp += new_elements[i+j] - new_elements[j]
```

이제 매번 `sum(slice)`를 호출하지 않으므로 전체 시간 복잡도가 `O(n^2)`로 줄어든다. 실제로 `n = 1000` 랜덤 케이스 기준으로 기존 풀이는 약 1.67초, 개선한 풀이는 약 0.07초 정도로 크게 좋아졌다.

남은 개선점은 가독성이다. `i`, `j`, `tmp`도 동작은 문제없지만, 이 문제에서는 길이와 시작 위치가 핵심 개념이므로 변수명을 더 구체적으로 쓰면 이해하기 쉽다.

```python
length
start
window_sum
```

또한 길이 1짜리 합을 `set(elements)`로 미리 넣는 방식도 맞지만, 길이 1부터 `n`까지를 같은 반복문에서 처리하면 풀이 흐름이 더 일관된다.

```python
for length in range(1, n + 1):
    window_sum = sum(doubled[:length])
    sums.add(window_sum)

    for start in range(1, n):
        window_sum += doubled[start + length - 1] - doubled[start - 1]
        sums.add(window_sum)
```

정답성과 성능은 이미 좋은 상태다. 마지막으로 다듬는다면 “길이별로 모든 시작점을 확인한다”는 의도가 코드에 더 잘 드러나도록 변수명과 반복문 구조를 정리하는 정도면 충분하다.
