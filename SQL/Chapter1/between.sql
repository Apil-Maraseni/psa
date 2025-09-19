-- The BETWEEN operator is used in a WHERE clause to filter the result set within a certain range. The range must be separated by an AND keyword.

select * 
from shows
where year
between 2020 and 2025;

-- When the values are text, BETWEEN filters the result within the alphabetical range.

SELECT *
FROM shows
WHERE name
BETWEEN 'A' AND 'D';

/*Note: BETWEEN stops at the second letter, but doesn’t include values that begin with the second letter.

So if a show’s title is just 'D', it would be returned, whereas 'Dragon Ball Super' will not.*/

select *
from shows
where release_year
between 1999 and 2024;

/* The New Golden Age of Television is considered to have begun in 1999 with Jersey mobster show, “The Sopranos”.

Find all shows released in the Golden Age, from 1999 to 2024. Have you seen any of those?*/