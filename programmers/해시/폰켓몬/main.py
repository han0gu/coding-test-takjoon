from collections import Counter

def solution(nums):
    c = Counter(nums)
    keys = c.keys()
    len_keys = len(keys)
    
    return len_keys if len_keys <= len(nums) // 2 else len(nums) // 2