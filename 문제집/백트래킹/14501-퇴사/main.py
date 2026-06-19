n = int(input())
candidates = [tuple(map(int, input().split())) for _ in range(n)] # need, profit

answer = 0
stack = [] # nxt_idx, cur_acc

# 첫 업무
for idx, (need, profit) in enumerate(candidates):
    if idx + need - 1 < n:
        stack.append((idx + 1, 0)) # 미선택
        stack.append((idx + need, profit)) # 선택
        break
# print('init stack', stack)

while stack:
    nxt_idx, cur_acc = stack.pop()

    if nxt_idx == n:
        answer = max(answer, cur_acc)
        continue

    nxt_need, nxt_profit = candidates[nxt_idx]

    if nxt_idx + nxt_need - 1 < n:
        stack.append((nxt_idx + 1, cur_acc)) # 미선택
        stack.append((nxt_idx + nxt_need, cur_acc + nxt_profit)) # 선택
    else:
        stack.append((nxt_idx + 1, cur_acc)) # 미선택
    # print('stack', stack)

print(answer)