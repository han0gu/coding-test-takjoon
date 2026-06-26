from collections import defaultdict

def solution(genres, plays):
    answer = []

    d = defaultdict(lambda: {'total':0, 'songs':[]})
    # print('d', d)

    for i, genre in enumerate(genres):
        d[genre]['songs'].append((i, plays[i]))
        d[genre]['total'] += plays[i]
    # print('d', d)

    sorted_genres = sorted(d, key=lambda x: -d[x]['total'])
    # print('sorted_keys', sorted_keys)

    for genre in sorted_genres:
        songs = d[genre]['songs']
        songs.sort(key=lambda x: (-x[1], x[0]))
        # print('songs', songs)

        for i in range(min(2, len(songs))):
            answer.append(songs[i][0])

    return answer
