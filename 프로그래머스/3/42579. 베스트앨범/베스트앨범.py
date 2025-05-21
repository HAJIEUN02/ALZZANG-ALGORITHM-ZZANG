def solution(genres, plays):
    answer = []
    song = dict() # 장르별 노래 index
    count = dict() # 장르별 총 재생
    
    # song 딕셔너리에 장르별 인덱스 저장
    for i in range(len(genres)):
        if song.get(genres[i], 0) == 0: # 딕셔너리에 장르 키가 없을 때
            song.update({genres[i] : [(i, plays[i])]})
            count.update({genres[i] : plays[i]})
        else: # 딕셔너리에 장르 키가 있을 때
            song[genres[i]].append((i, plays[i]))
            count[genres[i]] = count[genres[i]] + plays[i]
    
    sort_count = sorted(count.items(), key = lambda x: x[1], reverse = True)
    
    # 각 장르별로 곡 정렬 후 최대 2곡 선택
    for genre, _ in sort_count:
        # 1. 재생 수 내림차순
        # 2. 같으면 index 오름차순
        sorted_songs = sorted(song[genre], key=lambda x: (-x[1], x[0]))
        # 최대 2개까지 추가
        for i in range(min(2, len(sorted_songs))):
            answer.append(sorted_songs[i][0])
    
    return answer