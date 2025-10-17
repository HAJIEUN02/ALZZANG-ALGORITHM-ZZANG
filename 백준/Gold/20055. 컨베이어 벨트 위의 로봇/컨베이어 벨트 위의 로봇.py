from collections import deque
import sys

def solve_conveyor_robot():
    N, K = map(int, sys.stdin.readline().split())
    durabilities = list(map(int, sys.stdin.readline().split()))

    # durability: 2N 크기의 덱 (전체 벨트)
    durability = deque(durabilities)
    # robots: N 크기의 덱 (상단 벨트, robots[0] = 1번 칸, robots[N-1] = N번 칸)
    robots = deque([False] * N)
    
    step = 0

    # 2. 시뮬레이션 루프
    while True:
        step += 1
        
        ## 1단계: 컨베이어 벨트 한 칸 회전
        durability.rotate(1)  # 내구도 덱 회전
        robots.rotate(1)      # 로봇 위치 덱 회전
        
        # 회전 후 내리는 위치 (N번 칸, robots[N-1])에 도달한 로봇은 즉시 내림
        robots[N - 1] = False
        
        ## 2단계: 로봇 이동
        # N-2번 칸부터 1번 칸까지 (robots[N-2] -> robots[0]) 역순으로 검사
        for i in range(N - 2, -1, -1):
            current_pos = i     # 현재 로봇 위치 (덱 인덱스)
            next_pos = i + 1    # 이동할 다음 위치 (덱 인덱스)
            
            # 현재 위치에 로봇이 있고, 
            if robots[current_pos]:
                # 다음 칸에 로봇이 없으며 (robots[next_pos] == False),
                # 다음 칸의 내구도가 1 이상인 경우 (durability[next_pos] >= 1)
                if not robots[next_pos] and durability[next_pos] >= 1:
                    # 로봇 이동
                    robots[current_pos] = False
                    robots[next_pos] = True
                    # 내구도 감소
                    durability[next_pos] -= 1
                    
                    # 이동 후 내리는 위치 (N-1)에 도달하면 즉시 내림
                    if next_pos == N - 1:
                        robots[N - 1] = False
        
        ## 3단계: 로봇 올리기
        # 올리는 위치 (1번 칸, robots[0])에 로봇이 없고 내구도가 1 이상이면
        if not robots[0] and durability[0] >= 1:
            robots[0] = True       # 로봇 배치
            durability[0] -= 1     # 내구도 감소
            
        ## 4단계: 종료 조건 검사
        # 내구도가 0인 칸의 개수가 K개 이상인지 확인
        if durability.count(0) >= K:
            break
            
    return step

print(solve_conveyor_robot())