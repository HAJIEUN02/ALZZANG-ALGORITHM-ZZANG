def solution(n):
    array = []
    for i in range(1, n+1):
        if i%2 == 1:
            array.append(i)
    return array