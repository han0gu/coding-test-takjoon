#!/bin/python3

#
# Complete the 'maxDistinctSubstringLengthInSessions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sessionString as parameter.
#

def maxDistinctSubstringLengthInSessions(sessionString):
    if not sessionString:
        return 0
        
    splitted = sessionString.split('*')
    # print('splitted', splitted)
    if not splitted:
        return 0
    
    answer = 0
    for string in splitted:
        visited = []
        
        for c in string:
            if c in visited:
                break
            visited.append(c)
        
        answer = max(answer, len(visited))
        # print('visited', visited, answer)
        
    return answer
    

if __name__ == '__main__':
    sessionString = input()

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)
