# Compare BSTs for Equal Values but Different Structure 피드백

## 문제 조건 요약

- 문제 화면 PNG 기준으로 `100001`은 null sentinel이다.
- 두 트리는 null을 제외한 실제 노드 값의 multiset이 같아야 한다.
- 값 multiset이 같더라도 실제 트리 구조가 같으면 `0`, 구조가 다르면 `1`을 반환한다.

## `multiset` 해석

여기서 `same multiset of values`는 "짧은 리스트의 모든 원소가 긴 리스트에 포함된다"는 뜻이 아니다. **실제 노드 값의 종류와 개수까지 완전히 같아야 한다**는 뜻이다.

예를 들어 `100001`을 제외하고 보면 다음처럼 판단한다.

```text
[1, 2]       vs [1, 2, 3]    -> 값 multiset 다름
[1, 1, 2]    vs [1, 2, 2]    -> 값 multiset 다름
[4, 2, 5, 1, 3] vs [3, 1, 5, 2, 4] -> 값 multiset 같음
```

`root1 = [2, 1]`, `root2 = [1, 100001, 2]`는 원본 배열 길이는 다르지만, null을 제외한 값은 둘 다 `[1, 2]`다. 구조는 `2`의 왼쪽 자식이 `1`인 트리와 `1`의 오른쪽 자식이 `2`인 트리로 다르기 때문에 `1`이 맞다.

반대로 `root1 = [2, 1]`, `root2 = [2, 1, 100001]`는 trailing null만 추가된 형태라 실제 구조가 같다. 이 경우는 `0`이 맞다.

## 현재 풀이 리뷰

현재 풀이의 큰 방향은 맞다.

```python
real_idx_1 != real_idx_2 and sorted(real_value_1) == sorted(real_value_2)
```

- `100001`을 제외한 값만 모아 비교한다.
- 실제 값이 들어 있는 배열 인덱스 목록으로 구조 차이를 판단한다.
- 같은 값 multiset이면서 non-null 인덱스 패턴이 다르면 다른 구조로 본다.

이 문제의 배열 표현에서는 non-null 인덱스 패턴이 트리 구조를 나타내므로, 본문 조건 기준으로는 합리적인 접근이다.

다만 `trees-and-binary-search-trees` 섹션 문제라는 관점에서는 인덱스 리스트 비교보다 **트리 구조 비교**가 코드 의도를 더 잘 보여준다. 또한 값 multiset 비교는 정렬보다 `Counter`가 더 직접적이다.

## 시간 복잡도

현재 풀이에서 가장 큰 비용은 정렬이다.

```python
sorted(real_value_1) == sorted(real_value_2)
```

`root1` 길이를 `n`, `root2` 길이를 `m`이라고 하면:

```text
값/인덱스 수집: O(n + m)
인덱스 리스트 비교: O(min(n, m))
값 정렬: O(n log n) + O(m log m)
```

정확히는 실제 노드 수를 `a`, `b`라고 했을 때 `O(n + m + a log a + b log b)`이고, 최악의 경우에는 보통 `O(n log n + m log m)`이라고 말해도 된다.

`Counter`를 쓰면 각 원소를 한 번씩 세므로 평균 시간 복잡도는 `O(n + m)`이다. 딕셔너리를 만드는 비용도 각각 평균 `O(n)`, `O(m)`으로 보면 된다.

## Best-practice 예시

아래 코드는 문제 본문 조건에 충실한 개선 예시다. 값 비교는 `Counter`, 구조 비교는 재귀로 null/non-null 모양만 확인한다.

```python
from collections import Counter

NULL = 100001

def verifySameMultisetDifferentStructure(root1, root2):
    values1 = [value for value in root1 if value != NULL]
    values2 = [value for value in root2 if value != NULL]

    if Counter(values1) != Counter(values2):
        return 0

    def same_structure(arr1, arr2, idx1, idx2):
        node1_is_null = idx1 >= len(arr1) or arr1[idx1] == NULL
        node2_is_null = idx2 >= len(arr2) or arr2[idx2] == NULL

        if node1_is_null or node2_is_null:
            return node1_is_null and node2_is_null

        left_same = same_structure(arr1, arr2, idx1 * 2 + 1, idx2 * 2 + 1)
        right_same = same_structure(arr1, arr2, idx1 * 2 + 2, idx2 * 2 + 2)

        return left_same and right_same

    if same_structure(root1, root2, 0, 0):
        return 0

    return 1
```

이 방식의 장점은 다음과 같다.

- 값 multiset 비교 의도가 `Counter`로 바로 드러난다.
- 구조 비교가 "값이 같은지"가 아니라 "노드가 있는 위치가 같은지"를 기준으로 동작한다.
- 정렬을 쓰지 않아 전체 평균 시간 복잡도가 `O(n + m)`이다.
- 트리 문제에서 중요한 null/child 구조를 코드로 직접 표현한다.

## HackerRank 숨은 테스트 주의

현재 1개 테스트만 실패한다면 코드 논리보다 HackerRank 채점 데이터 문제일 가능성이 있다. 외부 보고에 따르면 이 문제는 본문 예제로 제시된 케이스와 숨은 테스트의 기대값이 충돌하는 사례가 있다.

본문 예시:

```text
root1 = [4, 2, 5, 1, 3, 100001, 100001]
root2 = [3, 1, 5, 100001, 2, 4, 100001]
```

문제 설명대로라면 실제 값 multiset은 같고 구조는 다르므로 `1`이 맞다. 만약 숨은 테스트가 이 케이스를 `0`으로 기대한다면, 그것은 풀이 문제가 아니라 채점 케이스 문제로 봐야 한다.

참고:

- <https://www.linkedin.com/posts/pawel-kornecki-66a621b5_isnt-this-a-bit-suspicious-a-problem-marked-activity-7457740568333553665-4vRj>
- <https://medium.com/%40vgudapati/conversation-with-hacker-rank-ai-tutor-5183e79cd6a4>

## 다음 문제에 적용할 교훈

트리 문제에서는 배열 길이보다 먼저 **null을 포함한 구조 표현**을 봐야 한다. 값 비교는 값 비교대로 분리하고, 구조 비교는 null/non-null 패턴 또는 실제 child 관계를 따라가며 따로 비교하면 실수를 줄일 수 있다.
