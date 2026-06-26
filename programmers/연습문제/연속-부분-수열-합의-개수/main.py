def solution(elements):
    sums = set()
    n = len(elements)
    doubled = elements * 2

    for length in range(1, n + 1):
        window_sum = sum(doubled[:length])
        sums.add(window_sum)

        for start in range(1, n):
            window_sum += doubled[start + length - 1] - doubled[start - 1]
            sums.add(window_sum)

    return len(sums)
