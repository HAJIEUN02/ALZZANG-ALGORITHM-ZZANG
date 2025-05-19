def solution(phone_book):
    phone_set = set(phone_book)  # 모든 번호를 set에 저장 O(N)

    for phone in phone_book:
        for i in range(1, len(phone)):  # 접두사 길이 1부터 len(phone)-1까지
            if phone[:i] in phone_set: # 접두어 만들기 phone[:i]는 O(i), 찾는 건 O(1)
                return False  # 접두어가 존재함
    return True  # 접두어가 없음
