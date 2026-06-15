# Write your MySQL query statement below
select e1.name as employee from employee e1 where e1.salary > 
( select e2.salary from employee e2 where e1.managerid = e2.id)