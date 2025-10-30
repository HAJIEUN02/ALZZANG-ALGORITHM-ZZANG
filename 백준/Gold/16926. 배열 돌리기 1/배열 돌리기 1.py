import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)
    
"""
테두리 돌리기를 반복
"""
groups = min(N, M) // 2

for i in range(groups):
    # 왼쪽 위, 오른쪽 아래 경계 좌표
    r_min, c_min = i, i
    r_max, c_max = N-1-i, M-1-i
    
    # 껍데기의 둘레 길이 계산
    perimeter_len = 2 * ((r_max - r_min) + (c_max - c_min))
    
    # 실제 회전 횟수(중앙값인 경우 회전 X)
    if perimeter_len == 0:
        continue
    rotation_count = R % perimeter_len
    
    # 실제 회전 횟수만큼 방복
    for _ in range(rotation_count):
        temp = A[r_min][c_min]
        
        # 1. 윗 변 (오른쪽 -> 왼쪽으로 덮어쓰기)
        # c_min부터 c_max-1까지 증가하며, A[c] <- A[c+1] 
        for c in range(c_min, c_max):
            A[r_min][c] = A[r_min][c + 1]
            
        # 2. 오른쪽 변 (아래 -> 위로 덮어쓰기)
        # r_min부터 r_max-1까지 증가하며, A[r] <- A[r+1] 
        for r in range(r_min, r_max):
            A[r][c_max] = A[r + 1][c_max]
            
        # 3. 아랫 변 (왼쪽 -> 오른쪽으로 덮어쓰기)
        # c_max부터 c_min+1까지 감소하며, A[c] <- A[c-1]
        for c in range(c_max, c_min, -1):
            A[r_max][c] = A[r_max][c - 1]
        
        # 4. 왼쪽 변 (위 -> 아래로 덮어쓰기)
        # r_max부터 r_min+1까지 감소하며, A[r] <- A[r-1]
        for r in range(r_max, r_min, -1):
            A[r][c_min] = A[r - 1][c_min]
          
        A[r_min+1][c_min] = temp
        
for row in A:
    print(*(row))