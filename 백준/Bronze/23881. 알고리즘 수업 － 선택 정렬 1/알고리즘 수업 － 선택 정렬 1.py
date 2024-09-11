"""의사코드
1. 배열 크기 N과 교환 횟수 K를 입력 받는다.
2. 배열의 값 N개를 입력받는다. 
3. N-2번째, N-3번째, N-4번째...0번째 원소의 크기를 비교한다.
4. 가장 큰 원소와 N-1번째 원소의 자리를 바꾸고 교환 횟수 K를 증가시킨다.(같은 경우 바꾸지 않음)
5. N-3번째, N-4번째, N-5번째...0번째 원소를 비교한다.
6. 가장 큰 원소와 N-2번째 원소의 자리를 바꾸고 교환 횟수 K를 증가시킨다.(같은 경우 바꾸지 않음)
...
7. 1번째 원소와 0번째 원소를 비교한다.
8. 더 큰 원소와 1번째 원소의 자리를 바꾸고 교환 횟수 K를 증가시킨다.(같은 경우 바꾸지 않음)
"""

num, exchange = map(int, input().split())
array = list(map(int, input().split()))

def selection_sort(array, exchange):
    k = 0
    for i in range(num-1, 0, -1):
        max_index = i

        for j in range(i-1, -1, -1):
            if array[j] > array[max_index]:
                max_index = j

        if i != max_index:
             array[i], array[max_index] = array[max_index], array[i]
             k += 1
             if(k == exchange):
                print(array[max_index], array[i])
    
    if k < exchange:
        print(-1)

selection_sort(array=array, exchange=exchange)