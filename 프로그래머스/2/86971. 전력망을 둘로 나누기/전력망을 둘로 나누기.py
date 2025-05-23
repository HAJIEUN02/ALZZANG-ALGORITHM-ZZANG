from collections import deque

def solution(n, wires):
    graph = make_graph(wires)
    min = n
    for a, b in wires:
        # 간선 임시 제거
        graph[a].remove(b)
        graph[b].remove(a)
        
        count = bfs(graph, n, a)
        diff = abs((n - count) - count)
        
        if diff < min:
            min = diff
            
        # 간선 복구
        graph[a].append(b)
        graph[b].append(a)
        
    return min

def make_graph(wires):
    graph = dict()
    for connect in wires:
        if graph.get(connect[0], 0) == 0: # 해당 key가 없는 경우
            graph.update({connect[0] : [connect[1]]})
        else: # 해당 key가 있는 경우
            graph[connect[0]].append(connect[1])
            
        if graph.get(connect[1], 0) == 0: # 해당 key가 없는 경우
            graph.update({connect[1] : [connect[0]]})
        else: # 해당 key가 있는 경우
            graph[connect[1]].append(connect[0])
    return graph

def bfs(graph, n, start):
    count = -1
    
    q = deque()
    q.append(start)
    visited = [False] * (n + 1) # 송전탑 번호 그대로 활용 위해
    visited[start] = True
    count += 1
    
    while q:
        v = q.popleft()
        count += 1
        
        for top in graph[v]:
            if visited[top] == False:
                q.append(top)
                visited[top] = True
                
    return count
    