"""파이썬 시간초과 문제
<dictionary는 list보다 빠름.>
dictionary는 hash table(키-값 쌍을 저장하는 데이터 구조)을 이용하므로
테이블 요소를 조회하는 데에 필요한 평균 명령어 수가 테이블에 저장된 요소 수와 무관,
dictionary의 검색 시간 복잡도가 N에 영향받지 않는 O(1)
key의 해시값을 구한 후에 해시값에 속하는 bucket에 값을 저장함
list는 경우에 따라 O(logN)으로 구현됨.
"""
import sys

input = sys.stdin.readline
array_size, exchange = map(int, input().split())
array = list(map(int, input().split()))

# O(NlogN)의 sorted함수를 사용해 정렬
sorted_array = sorted(array)
dictionary = {}

for index, value in enumerate(array):
    dictionary[value] = index

def selection_sort():
    current_exchange = 0
    for i in range(array_size-1, -1,-1):
        if array[i] != sorted_array[i]:
            current_exchange += 1
            result = [array[i], sorted_array[i]]
            array[i], array[dictionary[sorted_array[i]]] = array[dictionary[sorted_array[i]]], array[i]
            dictionary[result[0]], dictionary[result[1]] = dictionary[result[1]], dictionary[result[0]]
            if current_exchange == exchange:
                print(result[0], result[1])
    if current_exchange < exchange:
        print(-1)

selection_sort()