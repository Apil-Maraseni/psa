SELECT * FROM shows
-- here * selects all the columns from the table shows but if we want only some portions then we ca just specify them as SELECT column1, column2, column3 and so on
SELECT name, genre, FROM shows
-- to avooid dublicates we use the keyword distinct
SELECT DISTINCT column_name
FROM table_name;

-- for filtering based on conditions we use the keyword WHERE
SELECT *
FROM shows
WHERE id = 23;

-- another eg 
SELECT *
FROM shows
WHERE year > 2000

-- we can uise the ewual not equal greater less greater equal to or less equal to and so on
