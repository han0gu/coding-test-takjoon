def solution(brown, yellow):
    
    total = brown + yellow
    
    # 가로 >= 세로
    for width in range(brown // 2, 2, -1):
        # total이 width로 나눠져야 함
        if total % width > 0:
            continue
            
        height = total // width
        
        if brown == (width * 2 + height * 2 - 4):
            return [width, height]