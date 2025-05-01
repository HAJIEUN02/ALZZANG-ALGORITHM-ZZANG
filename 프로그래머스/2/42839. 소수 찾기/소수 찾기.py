from itertools import permutations

def check_is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
        
    return True    

def solution(numbers):
    answer = 0
    p = []
    result = []
    
    for i in range(1, len(numbers)+1):
        p.extend(permutations(numbers, i)) # extend는 permutation 결과의 각 원소를 넣음
        result = [int(''.join(i)) for i in p]
    
    for i in set(result):
        if check_is_prime(i):
            answer+=1
            
    return answer