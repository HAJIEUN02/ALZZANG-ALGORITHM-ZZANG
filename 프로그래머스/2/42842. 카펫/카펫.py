def solution(brown, yellow):
    w, h = 3, 3
    
    for i in range(w, 2048):
        for j in range(h, 2048):
            if i < j:
                break
                
            if yellow == i * j - brown:
                if i * 2 + 2 * (j - 2) == brown and (i-2)*(j-2) == yellow:
                    answer = [i, j]
                    return answer

"""
w * 2 + (h - 2) * 2 = brown
(w - 2) * (h - 2) = yello
yellow = w * h - brown을 만족하는 w, h값 구하기
+) w >= h여야 함
"""