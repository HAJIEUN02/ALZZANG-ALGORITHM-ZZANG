from collections import deque

def solution(numbers, direction):
    answer = []
    q = deque(numbers)

    if direction == "left":
        pop_val = q.popleft()
        q.append(pop_val)
        answer = list(q)
        return answer
    elif direction == "right":
        pop_val = q.pop()
        q.appendleft(pop_val)
        answer = list(q)
        return answer
    else:
        return answer