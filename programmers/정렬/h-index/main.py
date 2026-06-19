def solution(citations):
    # 역순으로 정렬
    citations.sort(reverse=True)
    
    for _, v in enumerate(citations):
        # 현재 값을 인덱스로 하는 원소의 값이 현재 값 이상이라면 return
        if len(citations) >= v and citations[v-1] >= v:
            return v
    
    return 0