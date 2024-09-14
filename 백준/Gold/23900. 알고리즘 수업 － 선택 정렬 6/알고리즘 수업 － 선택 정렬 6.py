import sys

input = sys.stdin.readline

array_size = int(input())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

sorted_array_a = sorted(array_a)
dictionary = {}

def set_dictionary(arr_a, dic):
    for index, value in enumerate(arr_a):
        dic[value] = index

def selection_sort(arr_a, arr_b, sorted_a, arr_size, dic):
    if arr_a == arr_b:
        return(print(1))
    
    for i in range(arr_size-1, -1, -1):
        if arr_a[i] != sorted_a[i]:
            result = [arr_a[i], sorted_a[i]]
            arr_a[i], arr_a[dic[sorted_a[i]]] = arr_a[dic[sorted_a[i]]], arr_a[i]
            dic[result[0]], dic[result[1]] = dic[result[1]], dic[result[0]]
            if arr_a == arr_b:
                print(1)
                exit(0)
    
    return(print(0))

set_dictionary(arr_a=array_a, dic=dictionary)
selection_sort(arr_a=array_a, arr_b=array_b, sorted_a=sorted_array_a, arr_size=array_size, dic=dictionary)
