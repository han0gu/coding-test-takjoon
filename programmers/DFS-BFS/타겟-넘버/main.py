"""
각 자리마다 +- 두 가지 경우 가능 
-> 모든 조합의 경우의 수를 이진수로 구함
-> 계산 후 target과 일치하는지 판단
"""
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        tmp = 0

        for ch, n in zip(binary, numbers):
            tmp += n if ch == '1' else -1 * n
        if tmp == target:
            answer += 1
                
    return answer
    
    