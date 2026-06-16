# Write your MySQL query statement below
select 
query_name, 
round((sum(rating/position)/count(query_name)),2) as quality,
IFNULL(round(100*(select (count(*)/(select count(*) from queries q1 where q1.query_name = q2.query_name group by query_name)) from queries q2 where rating<3 and q2.query_name = q3.query_name group by q2.query_name),2),0) as poor_query_percentage
 from queries q3 group by query_name