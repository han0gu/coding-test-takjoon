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

    intervals.sort(key=lambda x: x[0])
    # print('sorted', intervals)

    answer = [intervals[0]]
    for cur_start, cur_end in intervals[1:]:
        target = answer[-1]
        _, target_end = target

        if cur_start <= target_end:
            answer[-1][1] = max(target_end, cur_end)
            # print('new target', target)
        else:
            answer.append([cur_start, cur_end])

    return answer

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
