#!/bin/python3

#
# Complete the 'binarySearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def binarySearch(nums, target):
    if not nums:
        return -1

    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        n = nums[mid]
        if n == target:
            return mid
        elif n < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
