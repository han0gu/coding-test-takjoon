from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    d = defaultdict(lambda: {'total':0, 'songs':[]})
    # print('d', d)
    
    for i, g in enumerate(genres):
        d[g]['songs'].append((i, plays[i]))
        d[g]['total'] += plays[i]
    # print('d', d)
    
    
    sorted_keys = sorted(d, key=lambda x: -d[x]['total'])
    # print('sorted_keys', sorted_keys)
    
    for key in sorted_keys:
        songs = d[key]['songs']
        songs.sort(key=lambda x: -x[1])
        # print('songs', songs)
        
        for i in range(min(2, len(songs))):
            answer.append(songs[i][0])
    
    return answer