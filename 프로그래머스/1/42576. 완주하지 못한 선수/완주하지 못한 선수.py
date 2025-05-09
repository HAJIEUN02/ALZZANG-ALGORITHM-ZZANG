def solution(participant, completion):
    count_dict = dict()
    for i in participant:
        count_dict[i] = count_dict.get(i, 0) + 1 # get : 딕셔너리에 있으면 value, 없으면 0 return
    
    # print(count_dict)

    for j in completion:
        count_dict[j] -= 1

    # print(count_dict)
    
    for key, value in count_dict.items():
        if value > 0:
            return key