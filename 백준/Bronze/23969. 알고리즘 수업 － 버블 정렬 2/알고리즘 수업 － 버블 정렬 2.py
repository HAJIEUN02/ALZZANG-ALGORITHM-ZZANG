"""
1. 0번째와 1번째 비교
2. 1번째와 2번째 비교
3. 2번째와 3번째 비교
...
4. n-2번째와 n-1번째 비교
=== 1회전 종료
...
1. 0번째와 1번째 비교
=== n-1회전 종료
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

def bubble_sort(array_size, exchange, array):
    current_exchange = 0
    for i in range(array_size-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                current_exchange += 1
                if current_exchange == exchange:
                    exit(print(*array))
    if current_exchange < exchange:
        print(-1)

bubble_sort(n, k, a)