from collections import deque

def solution(begin, target, words):
    answer = 0
    # target이 없는 경우 return 0
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))
    visited = [-1] * len(words)
    
    while q:
        word, idx = q.popleft()
        
        if word == target:
            return visited[idx] + 1
        
        for i in range(len(words)): # words 배열 모두 탐색
            if words[i] != begin and visited[i] == -1: # 시작 단어와 다르고 방문하지 않은 곳인 경우
                count = 0
                for c1, c2 in zip(word, words[i]): # 기준 단어와 탐색 단어를 비교했을 때 다른 경우
                    if c1 != c2:
                        count += 1
                        
                if count == 1:
                    q.append((words[i],i))
                    visited[i] = visited[idx] + 1

    return 0