from itertools import permutations

def solution(k, dungeons):
    sequence = []
    sequence.extend(permutations(dungeons, len(dungeons)))
    current_k = k
    
    current_count = 0
    answer = 0
    
    for cur_sequence in sequence:
        for cur_dungeon in range(len(dungeons)):
            # 최소 필요 피로도 cur_sequnce[cur_dungeon][0]
            # 소모 피로도 cur_sequnce[cur_dungeon][1]
            if current_k >= cur_sequence[cur_dungeon][0]:
                current_count += 1
                current_k -= cur_sequence[cur_dungeon][1]
            else:
                break
                
        if current_count > answer:
            answer = current_count
            
        current_k = k
        current_count = 0
        
    return answer

"""
현재 필요도 k, idx에 대해 최소 필요 피로도/소모 피로도 담긴 dungeons
던전 개수 1~8
최소 필요 피로도 >= 소모 피로도
최소 필요 피로도, 소모 피로도 모두 1 이상 1000 이하
"""