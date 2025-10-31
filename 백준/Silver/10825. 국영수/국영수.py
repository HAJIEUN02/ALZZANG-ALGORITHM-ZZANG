import sys
input = sys.stdin.readline

N = int(input())
students_score = []
for _ in range(N):
    line = input().split()
    name = line[0]
    korean = int(line[1])
    english = int(line[2])
    math = int(line[3])
    
    students_score.append((name, korean, english, math))

sorted_score = sorted(students_score, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(sorted_score[i][0])