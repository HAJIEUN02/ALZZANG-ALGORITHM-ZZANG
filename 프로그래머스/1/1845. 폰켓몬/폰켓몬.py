def solution(nums):
    dict = {}
    
    for i in nums:
        cur_val = dict.get(i, 0) # key값이 있으면 value를 가져오고, 없으면 0 가져옴
        dict.update({i : cur_val+1}) # cur_val(종류)별 개수 dict에 저장
    
    avaliable = len(nums)/2
    dict_size = len(dict)
    
    if dict_size >= avaliable:
        return avaliable
    else:
        return dict_size

"""
dict에 종류별 폰켓못 숫자 저장
가져갈 수 있는 폰켓못 수 len(nums)/2
len(dict)가 len(nums)/2보다 큰 경우 len(nums)/2 return
len(dict)가 len(nums)/2보다 작은 경우 len(dict) return
"""