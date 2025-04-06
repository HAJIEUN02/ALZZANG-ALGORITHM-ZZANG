import sys

# 최소 색종이 개수
ans = float('inf')

def dfs(paper, own_paper, used, x, y):
    global ans

    # 현재까지 사용한 색종이가 ans보다 크면 탐색 중단 (백트래킹)
    if used >= ans:
        return

    # 다음 1을 찾기
    for i in range(x, 10):
        for j in range(10):
            if paper[i][j] == 1:
                # 5x5부터 1x1까지 가능한 크기의 색종이를 시도
                for size in range(5, 0, -1):
                    if own_paper[size-1] > 0 and is_possible(paper, i, j, size):
                        # 색종이 붙이기
                        set_paper(paper, i, j, size, 0)
                        own_paper[size-1] -= 1

                        # 다음 DFS 호출 (현재 위치부터 탐색)
                        dfs(paper, own_paper, used + 1, i, j)

                        # 백트래킹 (원상 복구)
                        set_paper(paper, i, j, size, 1)
                        own_paper[size-1] += 1
                return  # 색종이를 붙일 곳을 찾았으면 이후 탐색 필요 없음

    # 모든 1을 덮었으면 최소 개수 갱신
    ans = min(ans, used)

def is_possible(paper, x, y, size):
    """size x size 색종이를 붙일 수 있는지 검사"""
    if x + size > 10 or y + size > 10:
        return False

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] == 0:
                return False
    return True

def set_paper(paper, x, y, size, val):
    """size x size 영역을 val(1 or 0)로 채움"""
    for i in range(x, x + size):
        for j in range(y, y + size):
            paper[i][j] = val

def main():
    global ans
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
    own_paper = [5] * 5  # 각 크기별 색종이 개수 (5장씩)

    dfs(paper, own_paper, 0, 0, 0)

    print(ans if ans != float('inf') else -1)

if __name__ == "__main__":
    main()
