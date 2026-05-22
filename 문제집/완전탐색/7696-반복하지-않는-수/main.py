def validate(number):
    digits = str(number)
    return len(digits) == len(set(digits))

while True:
    n = int(input())
    
    if n == 0:
        break

    answer = 0
    cnt = 0
    while cnt < n:
        answer += 1

        # 중복이 없는 수이면
        if validate(answer):
            # print('answer', answer)
            cnt += 1
    print(answer)


"""
python3 '문제집/완전탐색/7696-반복하지-않는-수/main.py' << 'EOF'
25
10000
0
EOF
"""