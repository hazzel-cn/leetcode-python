# Write your MySQL query statement below
SELECT Email FROM (SELECT Email,COUNT(*) AS ABC FROM Person GROUP BY Email) AS TB WHERE ABC > 1