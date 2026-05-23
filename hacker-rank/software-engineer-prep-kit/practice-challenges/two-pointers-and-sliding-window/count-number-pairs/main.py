#!/bin/python3

#
# Complete the 'countAffordablePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER budget
#

def countAffordablePairs(prices, budget):
    # print('prices', prices)
    # print('budget', budget)
    
    if len(prices) < 2:
        return 0
    
    answer_count = 0
    
    # print('a', prices[:len(prices) - 1])
    # print('b', prices[s + 1:])
    for s, s_value in enumerate(prices[:len(prices) - 1]):
        for e, e_value in enumerate(prices[s + 1:]):
            total = s_value + e_value
            # print('total', total)
            
            if total <= budget:
                answer_count += 1
            else:
                continue
            
    return answer_count

if __name__ == '__main__':
    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    budget = int(input().strip())

    result = countAffordablePairs(prices, budget)

    print(result)
