-- The LIKE operator can be used to search for a pattern in a column. It’s used in the WHERE clause:
select *
from shows
where names like 'T%'; 

--This statement filters the result to only include shows with names that begin with the letter 'T'.

-- The percentage sign % is a wildcard character that can be used with LIKE. You can use it to match characters to a pattern of your desired query.
-- post fix use of it matches values that begin with that letter and prefix use ensures it matches with the end

SELECT * 
FROM shows 
WHERE name LIKE '%the%';

-- Here, any show that contains the word "the" in its name will be returned.

-- example

select genre
from shows
WHERE genre like '%com%'
/* Suppose we are searching for a comedy show.
Select all the shows with the genre including pattern "com" for genres like sitcom, rom-com, stand-up comedy, etc.*/

