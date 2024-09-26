def solution(n, k):
    service = int(n/10)
    return n*12000 + (k-service)*2000
    