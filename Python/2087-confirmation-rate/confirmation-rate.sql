# Write your MySQL query statement below
SELECT 
    s.user_id,
    ROUND(COUNT(CASE WHEN action = 'confirmed' THEN 1 END) / COUNT(*), 2) AS confirmation_rate
FROM signups s left join confirmations c on c.user_id = s.user_id
GROUP BY s.user_id
ORDER BY s.user_id;