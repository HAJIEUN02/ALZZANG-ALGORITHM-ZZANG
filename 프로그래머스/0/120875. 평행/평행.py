from itertools import permutations

def solution(dots):
    for a, b, c, d in permutations(dots, 4):
        
        dx1 = b[0] - a[0]
        dy1 = b[1] - a[1]
        dx2 = d[0] - c[0]
        dy2 = d[1] - c[1]

        if dx1 * dy2 == dx2 * dy1:
            return 1
    return 0
