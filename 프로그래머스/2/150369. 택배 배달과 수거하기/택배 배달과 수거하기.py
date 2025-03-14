def solution(cap, n, deliveries, pickups):
    answer = 0

    delivery = deliveries[::-1]
    pickup = pickups[::-1]

    deliveryCnt = 0
    pickupCnt = 0

    for i in range (n):
        deliveryCnt += delivery[i]
        pickupCnt += pickup[i]

        while deliveryCnt > 0 or pickupCnt > 0:
            deliveryCnt -= cap
            pickupCnt -= cap
            answer += (n-i)*2

    return answer
