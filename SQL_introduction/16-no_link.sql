-- script that lists all records of the table second_table of the database
-- Don’t list rows without a name value
SELECT name, score FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;