"""
아이디어 1
10x10 이차원 배열의 index 값을 좌표로 이용,
전부 기본값을 0으로 설정하고 지나갈 때마다 값을 증가시킴.
시작점은 5,5
전부 증가된 후에 이차원 배열을 순회하면서 기본값이 0이 아닌 index가 몇 개인지 count를 증가
-> 다른 곳에서 출발해 같은 점에 도착하는 경우의 경로 고려 X

아이디어 2 ->
set을 이용한 중복 제거
"""
def check_is_not_available(x, y):
    if x < 0 or y < 0 or x > 10 or y > 10:
        return 1
    else:
        return 0

def update_location(x, y, dir):
    if dir == "U":
        nx, ny = x, y + 1
    elif dir == "D":
        nx, ny = x, y - 1
    elif dir == "L":
        nx, ny = x - 1, y
    elif dir == "R":
        nx, ny = x + 1, y
    return nx, ny

def solution(dirs):
    x, y = 5, 5
    answer = set()
    
    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        if check_is_not_available(nx, ny):
            continue
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny
        
    return len(answer)/2