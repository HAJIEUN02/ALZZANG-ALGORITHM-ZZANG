def solution(n, lost, reserve):
    # 중복 제거 (자기 옷 있는 사람은 제외)
    lost_set = set(lost)
    reserve_set = set(reserve)
    intersection = lost_set & reserve_set

    lost = sorted(lost_set - intersection)
    reserve = sorted(reserve_set - intersection)

    for i in lost[:]:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            lost.remove(i)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            lost.remove(i)

    return n - len(lost)
