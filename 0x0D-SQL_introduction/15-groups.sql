-- lists the number of records with the same score
-- in second_table of htbn_0c_0

SELECT score, count(score) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
