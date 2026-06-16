# Write your MySQL query statement below
select activity_date as day,
count(distinct user_id) as active_users
 from activity
 WHERE activity_date BETWEEN date_add('2019-07-27', interval -29 day) AND '2019-07-27' group by activity_date
