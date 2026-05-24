#!/bin/python3

#
# Complete the 'getTopKFrequentEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY events
#  2. INTEGER k
#

def getTopKFrequentEvents(events, k):
    
    if not events or k == 0:
        return []
        
    # visited = [] # order
    cnt_map = {} # count
    for e in events:
        # if e not in visited:
        #     visited.append(e)
            
        if e not in cnt_map:
            cnt_map[e] = 1
        else:
            cnt_map[e] += 1
    # print('visited', visited)
    # print('cnt_map', cnt_map)
    
    sorted_cnt_map = sorted(cnt_map, key=lambda x: cnt_map[x], reverse=True)
    # print('sorted_cnt_map', sorted_cnt_map)
            
    return sorted_cnt_map[:k]

if __name__ == '__main__':
    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    k = int(input().strip())

    result = getTopKFrequentEvents(events, k)

    print('\n'.join(map(str, result)))
