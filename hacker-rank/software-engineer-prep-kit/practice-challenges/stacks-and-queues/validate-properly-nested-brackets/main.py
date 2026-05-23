#!/bin/python3

#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

open_brackets = ['(', '{', '[']
close_brackets = [')', '}', ']']

def areBracketsProperlyMatched(code_snippet):
    # print('code_snippet', code_snippet)
    
    stack = []
    
    for ch in code_snippet:
        if ch in open_brackets:
            stack.append(ch)
        elif ch in close_brackets:
            if stack and close_brackets.index(ch) == open_brackets.index(stack[-1]):
                stack.pop()
            else:
                return 0
        else:
            continue
            
    return 1 if len(stack) == 0 else 0

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
