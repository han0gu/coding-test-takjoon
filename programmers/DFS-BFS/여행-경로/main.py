from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)

    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)

    stack = ["ICN"]
    route = []

    while stack:
        cur_airport = stack[-1]

        if graph[cur_airport]:
            stack.append(graph[cur_airport].pop())
        else:
            route.append(stack.pop())

    return route[::-1]
