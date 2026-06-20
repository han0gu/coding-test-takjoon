def solution(n):
    b = str(bin(n)[2:])
    b_one_cnt = len([c for c in b if c == '1'])
    
    for i in range(n + 1, n * 4):
        b_i = str(bin(i)[2:])
        b_i_one_cnt = len([c for c in b_i if c == '1'])
        
        if b_one_cnt == b_i_one_cnt:
            return int(b_i, 2)