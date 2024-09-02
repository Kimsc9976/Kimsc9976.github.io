-- 코드를 입력하세요
SELECT
    MCDP_CD AS '진료과코드',
    count(date_format (APNT_YMD, '%Y-%m')) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05-%'
GROUP BY MCDP_CD
ORDER BY count(date_format (APNT_YMD, '%Y-%m')) ASC, MCDP_CD ASC