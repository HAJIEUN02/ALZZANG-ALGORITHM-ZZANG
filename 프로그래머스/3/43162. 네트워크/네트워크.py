"""
0번 컴퓨터랑 이어진 index번 컴퓨터 q에 저장(본인 제외)
q에 저장된 내용 싹다 꺼내오면서 이어진 index번 컴퓨터 q에 계속 저장
q가 빌 때까지 저장하면 0번 컴퓨터랑 이어진 네트워크 탐색 종료
방문한 곳은 다 visited 처리

1번 컴퓨터랑 이어진 index번 컴퓨터 q에 저장(visited 되지 않은 곳)
...
"""
from collections import deque

# 1개의 컴퓨터에 대해서 네트워크 찾기
def bfs_find_network(n, com, computers, visited):
    q = deque()
    q.append(com)
    visited[com] = True
    
    while q:
        v = q.popleft()
        
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            bfs_find_network(n, i, computers, visited)
            answer += 1
    
    return answer
