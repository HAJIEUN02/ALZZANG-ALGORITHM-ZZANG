"""의사코드
1. 배열 크기와 찾고자 하는 교환 횟수를 입력받는다.
2. 배열 원소들을 입력받는다.
3. max_index를 N-1(배열의 마지막 index)로 설정한다.
4. N-2번째, N-3번째, N-4번째...0번째 원소와
max_index번째 원소를 비교하여 값이 더 큰 경우 해당 index를 max_index로 설정한다.
5. N-2번째부터 0번째 원소까지 전부 비교했을 때 max_index 값이 N-1의 값보다 큰 경우 swap하고
교환 횟수를 증가시킨다.
5-1. 증가한 교환횟수가 입력받은 수와 같다면 교환 발생 직후의 배열을 출력하고 정렬을 종료한다.
...
6. max_index를 1로 설정한다.
7. 0번째 원소와 max_index번째 원소를 비교하여...
...
8. 정렬이 완료되었는데 교환 횟수가 처음에 입력받은 수보다 작다면 -1을 출력한다.
"""

array_size, exchange = map(int, input().split())
array = list(map(int, input().split()))

def selection_sort():
    sort_exchange = 0
    for i in range(array_size-1, 0, -1):
        max_index = i

        for j in range(i-1, -1, -1):
            if(array[j] > array[max_index]):
                max_index = j

        if(i != max_index):
            array[max_index], array[i] = array[i], array[max_index]
            sort_exchange += 1
            if(sort_exchange == exchange):
                print(*array)
            
    if(sort_exchange < exchange):
        print(-1)

selection_sort()