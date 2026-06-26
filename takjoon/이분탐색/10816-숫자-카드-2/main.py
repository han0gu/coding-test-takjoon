from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
# print('have_list', have_list)

m = int(input())
m_list = list(map(int, input().split()))
# print('target_list', target_list)

counter = Counter(n_list)
# print('counter', counter)

answer = [None] * m
for i, target in enumerate(m_list):
    answer[i] = str(counter[target])

print(" ".join(answer))