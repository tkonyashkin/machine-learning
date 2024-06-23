SELECT  f.post_id
       ,f.time
       ,u.age
       ,u.os
FROM "feed_action" f
INNER JOIN "user" u
ON f.user_id = u.id
WHERE u.city = 'Omsk'
AND f.action = 'like'
ORDER BY f.time DESC
LIMIT 10