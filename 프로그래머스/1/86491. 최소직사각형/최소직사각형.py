def solution(sizes):
    pw, ph = sizes[0][0], sizes[0][1]
    answer = pw*ph
    
    for i in range(1, len(sizes)):
        fw, fh = compare_size(pw, ph, sizes[i][0], sizes[i][1])
        sw, sh = compare_size(pw, ph, sizes[i][1], sizes[i][0])
        
        if fw*fh > sw*sh:
            pw, ph = sw, sh
        else : 
            pw, ph = fw, fh
        
        answer = pw*ph
        
    return answer

def compare_size(prev_w, prev_h, cur_w, cur_h):
    w, h = prev_w, prev_h
    if prev_w < cur_w:
        w = cur_w
    if prev_h < cur_h:
        h = cur_h
    return w, h

"""
i-1의 가로, 세로와 i의 가로, 세로를 비교해서 결정된 명함의 가로, 세로  return 
i-1의 가로, 세로와 i의 세로, 가로를 비교해셔 결정된 명함 가로, 세로 return
return된 가로 세로의 넓이를 계산해서 더 작게 나온 명함의 가로, 세로 값으로 h, w 갱신
"""