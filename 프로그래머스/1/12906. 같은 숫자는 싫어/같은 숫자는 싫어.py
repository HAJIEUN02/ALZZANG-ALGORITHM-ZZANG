def solution(arr):
    result = []
    prev = -1
    copy_arr = arr[:]
    n = len(arr)
    
    for i in range(0, n):
        if copy_arr[i] != prev:
            result.append(copy_arr[i])
            
        prev = copy_arr[i]
        
    return result