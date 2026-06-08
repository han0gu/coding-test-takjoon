from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
# print('have_list', have_list)

target = int(input())
m_list = list(map(int, input().split()))
# print('target_list', target_list)

counter = Counter(n_list)
# print('counter', counter)

answer = ''
for i, m in enumerate(m_list):
    answer += str(counter[m]) if counter[m] else '0'

print(" ".join(answer))