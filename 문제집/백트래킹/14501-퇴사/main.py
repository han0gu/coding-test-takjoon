# 선택 가능 여부 판단
def can_handle(idx, need, limit, occupied):
    for i in range(idx, idx + need):
        if i in occupied:
            return False
    
    return idx + need <= limit

    

n = int(input())
candidates = [tuple(map(int, input().split())) for _ in range(n)] # need, profit

answer = 0
stack = [] # idx, acc, occupied

# start point
for idx, (need, profit) in enumerate(candidates):
    if can_handle(idx, need, n, []):
        # 미선택
        stack.append( (idx, 0, []) )

        # 선택
        nxt_occ = []
        for i in range(idx, idx + need):
            nxt_occ.append(i)
        stack.append( (idx, profit, nxt_occ) )
        
        break
# print('init stack', stack)

while stack:
    cur_idx, cur_acc, cur_occupied = stack.pop()

    # 모두 검토한 경우
    if cur_idx == n - 1:
        answer = max(answer, cur_acc)
        continue

    # 다음 옵션 미선택
    nxt_idx = cur_idx + 1
    nxt_need, nxt_profit = candidates[nxt_idx]
    stack.append( (nxt_idx, cur_acc, cur_occupied) )
    
    # 기간 내 처리 가능한 경우
    if can_handle(nxt_idx, nxt_need, n, cur_occupied):
        # 다음 옵션 선택
        nxt_occupied = [*cur_occupied]
        for i in range(nxt_idx, nxt_idx + nxt_need):
            nxt_occupied.append(i)

        stack.append( (nxt_idx, cur_acc + nxt_profit, nxt_occupied) )
        # print('\nstack', stack)

print(answer)