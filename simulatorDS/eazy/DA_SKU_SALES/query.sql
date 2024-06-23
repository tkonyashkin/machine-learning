SELECT
  cal_date AS days,
  sum(cnt) AS sku
FROM
  transactions_another_one
GROUP by
  cal_date