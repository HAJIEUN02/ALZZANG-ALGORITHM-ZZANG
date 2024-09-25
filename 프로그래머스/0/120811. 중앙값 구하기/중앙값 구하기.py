def solution(array):
    sorted_array = sorted(array)
    center_index = int(len(array)/2)
    return sorted_array[center_index]