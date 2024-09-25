def solution(array, height):
    sorted_array = sorted(array)
    count = 0
    for index, value in enumerate(sorted_array):
        if value > height:
            count += 1
            
    return count