from collections import Counter


def solution(k, tangerine):
    counts = sorted(Counter(tangerine).values(), reverse=True)

    answer = 0
    for count in counts:
        k -= count
        answer += 1

        if k <= 0:
            return answer

    return answer
