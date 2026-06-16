from collections import deque

def solution(bridge_length, weight_limit, truck_weights):
    answer = 0 # 최소 몇 초 걸리냐
    
    remain_trucks = deque(truck_weights)
    bridge_q = deque()
    # print('remain_trucks', remain_trucks)
    # print('bridge_q', bridge_q)
    
    # 모든 트럭이 건널 때까지
    while remain_trucks or bridge_q:
        # print('remain_trucks', remain_trucks)
        # print('bridge_q', bridge_q)
        
        answer += 1
        
        # 다리 위의 모든 트럭 진행도 +1
        for i, truck in enumerate(bridge_q):
            weight, process = truck
            bridge_q[i] = (weight, process + 1)
            
        # 다리 위 첫번째 트럭의 완료 여부 판단
        if bridge_q and bridge_q[0][1] > bridge_length:
            bridge_q.popleft()
        
        # 남은 트럭 중 첫번째 트럭이 다리에 올라갈 수 있는지 판단
        if remain_trucks and sum([w for w, _ in bridge_q]) + remain_trucks[0] <= weight_limit:
            bridge_q.append( (remain_trucks[0], 1) )
            remain_trucks.popleft()

    return answer
    