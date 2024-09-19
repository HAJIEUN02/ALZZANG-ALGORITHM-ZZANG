import sys

input = sys.stdin.readline

count = 0
loop = 1

for i in range(1999):
    n = int(input())
    count += n

    if n == -1:
        count += 1
        print(count)
        exit(0)