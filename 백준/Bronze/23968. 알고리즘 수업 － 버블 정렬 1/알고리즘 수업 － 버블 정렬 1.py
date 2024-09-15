""" <from front>
1. 0번째 원소와 1번째 원소를 비교한다.(0번째 원소가 더 크면 swap)
2. 1번째 원소와 2번째 원소를 비교한다.(1번째 원소가 더 크면 swap)
3. 2번째 원소와 3번째 원소를 비교한다.(2번째 원소가 더 크면 swap)
…
4. n-2번째 원소와 n-1번째 원소를 비교한다.(n-2번째 원소가 더 크면 swap)
=========== 1회전 종료
1. 0번째 원소와 1번째 원소를 비교한다.(0번째 원소가 더 크면 swap)
2. 1번째 원소와 2번째 원소를 비교한다.(1번째 원소가 더 크면 swap)
3. 2번째 원소와 3번째 원소를 비교한다.(2번째 원소가 더 크면 swap)
…
4. n-3번째 원소와 n-2번째 원소를 비교한다.(n-3번째 원소가 더 크면 swap)
=========== 2회전 종료
…
1. 0번째 원소와 1번째 원소를 비교한다.(0번째 원소가 더 크면 swap)
=========== n-1회전 종료
"""
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))

def bubble_sort(array_size, exchange, array):
    current_exchange = 0
    for i in range(array_size-2, -1, -1):
        for j in range(i+1):
            if array[j] > array[j+1]: 
                array[j], array[j+1] = array[j+1], array[j]
                current_exchange += 1
                if current_exchange == exchange:
                    print(array[j], array[j+1])
                    exit(0)

    if current_exchange < exchange:
        print(-1)

    
bubble_sort(n, k, a)