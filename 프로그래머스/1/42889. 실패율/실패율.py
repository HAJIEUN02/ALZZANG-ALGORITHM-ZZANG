"""
stages를 순회.
N+2 크기의 clear_person 리스트를 선언
clear_person[1]에는 1stage에 머무르는 사람 수(1 stage 실패)
clear_person[1]에는 2stage에 머무르는 사람 수(1 stage 성공, 2stage 실패)
clear_person[2]에는 3stage에 머무르는 사람 수(1,2 stage 성공, 3stage 실패)
clear_person[3]에는 4stage에 머무르는 사람 수(1,2,3 stage 성공, 4stage 실패)
clear_person[4]에는 5stage에 머무르는 사람 수(1,2,3,4 stage 성공, 5stage 실패)
clear_person[5]에는 6stage에 머무르는 사람 수(1,2,3,4,5 stage 성공)
...
count 수 업데이트 -> O(n), 최대 20만번 연산

clear_person을 순회.
total_clear = len(stages)
-> if clear_person[i] = 0인 경우, 즉시 failure[i] = 0으로 정의 후 다음 loop
failure[1]에 1stage 실패율 : clear_person[1]/total_clear, total_clear-=clear_person[1]
failure[2]에 2stage 실패율 : clear_person[2]/total_clear, total_clear-=clear_person[2]
....
O(n), 최대 500번 연산

failure 딕셔너리의 value인 실패율을 기준으로 
sorted(reverse=True)로 정렬해서 출력 -> O(nlogn)
"""
def solution(N, stages):
    challenger = [0] * (N+2)
    for stage in stages:
        challenger[stage] +=1
    
    fails = {}
    total = len(stages)
    
    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]
            
    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    
    return result