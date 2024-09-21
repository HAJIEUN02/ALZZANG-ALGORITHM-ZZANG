def solution(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    count = [0] * 3
    
    # O(N)
    for i, answer in enumerate(answers): # O(N)
        for j, pattern in enumerate(patterns): # 3개의 고정된 패턴이므로 O(1)
            if answer == pattern[i % len(pattern)]: # O(1)
                count[j] += 1
    
    student = []
    
    # O(1)
    for i, score in enumerate(count):
        if score == max(count):
            student.append(i+1)
    
    return student