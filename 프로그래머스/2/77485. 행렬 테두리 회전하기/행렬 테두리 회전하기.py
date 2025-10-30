"""
(2, 2, 5, 4)
2행 2열~5행 4열
= 왼쪽 위 (1,1) ~ (4,3) 오른쪽 아래
= (x1-1, y1-1) ~ (x2-1, y2-1)

- 최솟값 저장할 배열 선언(len(query) 만큼)
- 공동으로 사용할 배열
- 아래 과정을 query마다 반복
1. 현재 위치 값 (x, y)를 temp에 저장
- 위치에 들어 있는 값과 min(초기값 10001)에 들어있는 값을 비교해 더 작은 경우 min값 갱신
2. for: 왼쪽 변
- y1-1 고정
- x1-1에서 x2-1까지 증가하면서 덮어쓰기
- temp 갱신, min 갱신
3. for: 아랫 변
- x2-1 고정
- y1-1에서 y2-1까지 증가하면서 덮어쓰기
- temp 갱신, min 갱신
4. for: 오른쪽 변
- y2-1 고정
- x2-1에서 x1-1까지 감소하면서 덮어쓰기
- temp 갱신, min 갱신
5. for: 위쪽 변
- x1-1 고정
- y2-1에서 y2-1까지 감소하면서 덮어쓰기
- temp 갱신, min 갱신
6. 한 query 배열에 대한 최솟값을 최솟값 저장할 리스트에 append
"""

def solution(rows, columns, queries):
    answer = []
    matrix = [
        [r * columns + c + 1 for c in range(columns)] 
        for r in range(rows)
    ]
    
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        
        temp = matrix[x1][y1]
        min_val = temp
        
        # 1. 왼쪽 변 (아래 -> 위로 덮어쓰기)
        for x in range(x1, x2):
            matrix[x][y1] = matrix[x + 1][y1]
            min_val = min(min_val, matrix[x][y1])
        
        # 2. 아랫 변 (오른쪽 -> 왼쪽으로 덮어쓰기)
        for y in range(y1, y2):
            matrix[x2][y] = matrix[x2][y + 1]
            min_val = min(min_val, matrix[x2][y])

        # 3. 오른쪽 변 (위 -> 아래로 덮어쓰기)
        # r2부터 r1+1까지 역순 순회
        for x in range(x2, x1, -1):
            matrix[x][y2] = matrix[x - 1][y2] 
            min_val = min(min_val, matrix[x][y2])
            
        # 4. 윗 변 (왼쪽 -> 오른쪽으로 덮어쓰기)
        # c2부터 c1+1까지 역순 순회
        for y in range(y2, y1, -1): 
            matrix[x1][y] = matrix[x1][y - 1]
            min_val = min(min_val, matrix[x1][y])
        
        matrix[x1][y1 + 1] = temp
        
        answer.append(min_val)
        
    print(matrix)
    
    return answer
