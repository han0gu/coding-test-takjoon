def solution(n):
    b = bin(n)[2:]
    b_one_cnt = b.count('1')

    i = n + 1
    while True:
        b_i = bin(i)[2:]
        b_i_one_cnt = b_i.count('1')

        if b_one_cnt == b_i_one_cnt:
            return i

        i += 1
