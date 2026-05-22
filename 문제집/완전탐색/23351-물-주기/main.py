"""
n개의 화분
"""
n, k, a, b = map(int, input().split())

flowers = [k] * n
# print('init flowers', flowers)

day = 0
water_start = 0
water_end = water_start + a - 1
while 0 not in flowers:
    day += 1

    water_start %= n
    water_end %= n
    if water_start != water_end:
        for i in range(water_start, water_end + 1):
            flowers[i] += b
    else:
        flowers[water_start] += b

    flowers = [f - 1 for f in flowers]

    # print(day, water_start, water_end, flowers)

    water_start += a
    water_end += a

print(day)

"""
python3 '문제집/완전탐색/23351-물-주기/main.py' << 'EOF'
6 3 2 2
EOF

python3 '문제집/완전탐색/23351-물-주기/main.py' << 'EOF'
2 2 1 1
EOF
"""