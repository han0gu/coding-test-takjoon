def solution(s):
    stack = []

    for c in s:
        if not stack:
            stack.append(c)
            continue

        head = stack[-1]
        if head == c:
            stack.pop()
        else:
            stack.append(c)

    return 1 if not stack else 0
