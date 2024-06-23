SELECT 
    sku, 
    dates, 
    AVG(price) AS price, 
    COUNT(*) AS qty
FROM 
    transactions
GROUP BY 
    sku, 
    dates