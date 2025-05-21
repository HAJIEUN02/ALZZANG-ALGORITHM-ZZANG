def solution(clothes):
    dict_clothes = dict()
    answer = 1
    
    for arr in clothes:
        if dict_clothes.get(arr[1], 0) == 0: # dict에 해당 key가 존재하지 않으면
            dict_clothes.update({arr[1]: [arr[0]]})
        else: #dict에 해당 key가 존재하면
            dict_clothes[arr[1]].append(arr[0])
    
    for key in dict_clothes:
        answer *= (len(dict_clothes[key]) + 1)
    
    return answer - 1 # 아무것도 안 입는 경우 빼주기

"""
딕셔너리에 종류(key), 이름(value)로 저장
key.append
get(key, 0)한 값이 0이면 update해주고 아니라면 dict[key].append(값)
"""