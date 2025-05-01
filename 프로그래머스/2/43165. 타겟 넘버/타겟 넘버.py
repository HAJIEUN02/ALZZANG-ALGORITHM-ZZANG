def solution(numbers, target):
    return bfs(numbers, target)

def bfs(numbers, target):
    value = [0]
    count = 0
    
    for num in numbers:
        temp = []
        for v in value:
            temp.append(v + num)
            temp.append(v - num)
        value = temp
    
    for i in value:
        if i == target:
            count += 1
    
    return count
    
    