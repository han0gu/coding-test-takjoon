def solution(n):
    answer = 1

    for i in range(1, n // 2 + 1):
        tmp = i
        for j in range(i + 1, n + 1):
            tmp += j
            if tmp >= n:
                if tmp == n:
                    answer += 1
                break

    return answer
