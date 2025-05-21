from collections import deque 

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    return bfs(n, m, maps)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n, m, maps): # (0,0) 출발, (n-1, m-1) 도착
    q = deque()
    q.append((0, 0))
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y]
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    
    # 도달 불가
    return -1
                
    
                

"""
0이면 벽
(0, 0)이 출발점
(n-1, m-1)이 도착점
"""