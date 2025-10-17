SELECT CAR_ID,
    # GROUP BY 사용하는 경우 임의의 한 행 검사하므로 집계 함수 사용해서 검사해줘야 함
    CASE WHEN SUM(
                CASE WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN 1
                ELSE 0
                END) > 0 THEN '대여중'
         ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;