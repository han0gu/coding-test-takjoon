#!/bin/python3

#
# Complete the 'maxDistinctSubstringLengthInSessions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sessionString as parameter.
#

def maxDistinctSubstringLengthInSessions(sessionString):
    answer = 0

    for session in sessionString.split('*'):
        start = 0
        visited = set()

        for end, ch in enumerate(session):
            while ch in visited:
                visited.remove(session[start])
                start += 1

            visited.add(ch)
            answer = max(answer, end - start + 1)

    return answer

if __name__ == '__main__':
    sessionString = input()

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)
