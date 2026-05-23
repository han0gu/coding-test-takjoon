#!/bin/python3

#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    # print('intervals', intervals)
    
    if not intervals:
        return []
    
    for i in intervals:
        i.sort()
        
    intervals.sort(key=lambda x: x[0])
    # print('sorted', intervals)
    
    answer = [intervals[0]]
    for i in range(1, len(intervals)):
        cur = intervals[i]
        cur_start = cur[0]
        cur_end = cur[1]
        # print('cur', cur_start, cur_end)
        
        target = answer[-1]
        target_start = target[0]
        target_end = target[1]
        # print('target', target_start, target_end)
        
        if cur_start <= target_end:
            answer[-1] = [target_start, max(target_end, cur_end)]
            # print('new target', target)
        else:
            answer.append(cur)
            
    return answer

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
