def solution(numbers):
    for index, value in enumerate(numbers):
        numbers[index] = value*2
    return numbers