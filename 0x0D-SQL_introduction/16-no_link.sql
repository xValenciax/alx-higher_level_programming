-- lists all records of second_table
-- of hbtn_0n_0 database

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
