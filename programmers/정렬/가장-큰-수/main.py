from functools import cmp_to_key


def compare(a, b):
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0


def solution(numbers):
    nums = [str(number) for number in numbers]
    nums.sort(key=cmp_to_key(compare))

    answer = ''.join(nums)
    return '0' if answer[0] == '0' else answer
