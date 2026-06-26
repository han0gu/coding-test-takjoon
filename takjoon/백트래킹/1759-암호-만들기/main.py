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

stack = [] # (검토한 마지막 인덱스, 선택한 문자 수, 선택한 문자 리스트)
stack = [
    (0, 0, ''),
    (0, 1, candidates[0])
]

while stack:
    cur_idx, selected_cnt, chars = stack.pop()

    if selected_cnt == L:
        if is_valid(chars):
            print(chars)
        continue

    if cur_idx == C - 1:
        continue

    # 다음 문자 미선택
    stack.append( (cur_idx + 1, selected_cnt, chars) )
    # 다음 문자 선택
    stack.append( (cur_idx + 1, selected_cnt + 1, chars + candidates[cur_idx + 1]) )