from itertools import combinations

L, C = map(int, input().split())
candidates = input().split()
candidates.sort()

moums = {'a','e','i','o','u'}
def is_valid(chars):
    cnt_moum = 0
    for c in chars:
        if c in moums:
            cnt_moum += 1
    return cnt_moum >= 1 and len(chars) - cnt_moum >= 2

answer = []
for comb in combinations(candidates, L):
    if is_valid(comb):
        print(''.join(comb))