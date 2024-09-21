def solution(numbers):
    array_size = len(numbers)

    if array_size < 2 or array_size > 100:
        return
    
    answer = []
    for i in range(array_size):
        if not 0 <= numbers[i] <= 100:
            sys.exit(0)
        for j in range(i+1, array_size):
            if not 0 <= numbers[i] <= 100:
                sys.exit(0)
            answer.append(numbers[i] + numbers[j])
    
    answer = list(set(answer))
    answer.sort()
    return answer