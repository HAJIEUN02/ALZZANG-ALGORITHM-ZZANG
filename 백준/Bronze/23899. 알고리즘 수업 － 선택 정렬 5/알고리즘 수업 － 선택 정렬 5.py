import sys

input = sys.stdin.readline
array_size = int(input())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

def selection_sort(arr_size, arrA, arrB):
    # 애초에 같은 것을 입력한 경우
    if arrA == arrB:
        return(print(1))

    for i in range(arr_size-1, 0, -1):
        max_index = i
        for j in range(i-1, -1, -1):
            if arrA[j] > arrA[max_index]:
                max_index = j
        if max_index != i:
            arrA[i], arrA[max_index] = arrA[max_index], arrA[i]
            if arrA == arrB:
                print(1)
                exit(0)
    return(print(0))
        
selection_sort(arr_size=array_size, arrA=arrayA, arrB=arrayB)