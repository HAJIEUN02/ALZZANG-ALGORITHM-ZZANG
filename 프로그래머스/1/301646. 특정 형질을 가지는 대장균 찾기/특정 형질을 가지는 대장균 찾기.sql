SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0  -- 2번 형질 없어야 함
  AND (GENOTYPE & 5) != 0; -- 1번(1)이나 3번(4) 형질 중 하나 이상 있어야 함