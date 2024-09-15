import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def bubble_sort(array_size, array_a, array_b):
    for i in range(array_size-1, 0, -1):
        for j in range(i):
            if array_a[j] > array_a[j+1]:
                array_a[j], array_a[j+1] = array_a[j+1], array_a[j]
                # 매번 array_a와 array_b 전부를 비교하면 시간이 오래 걸리므로,
                # 현재 index의 값이 같은지 먼저 확인한 후 array 전체를 비교
                if array_a[j] == array_b[j]:
                    if array_a == array_b:
                           print(1)
                           exit(0)
    print(0)

# 처음에 같은 정렬을 입력하는 경우도 생각할 것!
if a == b:
    print(1)
    exit(0)
else:
    bubble_sort(n, a, b)