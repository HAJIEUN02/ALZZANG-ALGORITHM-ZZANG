import sys

input = sys.stdin.readline
array_size, exchange = map(int, input().split())
array = list(map(int, input().split()))

sorted_array = sorted(array)
dictionary = {}

def setDictionary(arr, dic):
    for index, value in enumerate(array):
         dictionary[value] = index

def selection_sort(arr_size, arr, sorted_arr, dic, ex):
    current_exchange = 0
    for i in range(arr_size-1, -1, -1):
        if arr[i] != sorted_arr[i]:
            current_exchange += 1
            result = [arr[i], sorted_arr[i]]
            arr[i], arr[dic[sorted_arr[i]]] = arr[dic[sorted_arr[i]]], arr[i]
            dic[result[0]], dic[result[1]] = dic[result[1]], dic[result[0]]

            if current_exchange == ex:
                print(*arr)
    if current_exchange < ex:
        print(-1)

setDictionary(arr=array, dic=dictionary)
selection_sort(arr_size=array_size, arr=array, sorted_arr=sorted_array, dic=dictionary, ex=exchange)