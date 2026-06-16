from collections import deque

def solution(bridge_length, weight_limit, truck_weights):
    answer = 0 # 최소 몇 초 걸리냐

    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    cur_bridge_weight = 0

    while trucks or cur_bridge_weight > 0:
        answer += 1

        # 맨 왼쪽 트럭 처리
        cur_bridge_weight -= bridge.popleft()

        # 새로운 트럭 추가 시도
        if trucks:
            if cur_bridge_weight + trucks[0] <= weight_limit:
                cur_truck = trucks.popleft()
                bridge.append(cur_truck)
                cur_bridge_weight += cur_truck
            else:
                bridge.append(0)
        else:
            bridge.append(0)

    return answer
