#!/bin/python3

def findTaskPairForSlot(taskDurations, slotLength):
    # print('taskDurations', taskDurations)
    # print('slotLength', slotLength)

    if len(taskDurations) < 2 or slotLength < 2:
        return [-1, -1]

    visited = {}

    for i, value in enumerate(taskDurations):
        remain = slotLength - value

        if remain in visited:
            return [visited[remain], i]

        visited[value] = i

    return [-1, -1]

if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
