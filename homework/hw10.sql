-- CS 61A Fall 2014
-- Name:
-- Login:

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

create table dogs_sizes as
  select name as name, height as size from dogs;

-- The names of all "toy" and "mini" dogs
select name from dogs, sizes where (size = "toy" or size = "mini")
                                    and height > min and height <= max;
-- Expected output:
--   abraham
--   eisenhower
--   fillmore
--   grover
--   herbert

-- All dogs with parents ordered by decreasing height of their parent
select a.name from dogs_sizes as a, parents as b, dogs_sizes as c 
            where a.name=b.child and b.parent=c.name order by -c.size;
-- Expected output:
--   herbert
--   fillmore
--   abraham
--   delano
--   grover
--   barack
--   clinton

-- Sentences about siblings that are the same size
with
  siblings(first, second, first_size, second_size) as (
    select a.name, b.name, a.size, b.size 
      from dogs_sizes as a, dogs_sizes as b, parents as c, parents as d
        where a.name<b.name and a.name=c.child and b.name=d.child and c.parent=d.parent
  )
select first||" and "||second||" are "||size||" siblings" from siblings, sizes 
  where first_size>min and first_size<=max and second_size>min and second_size<=max
  ;
-- Expected output:
--   barack and clinton are standard siblings
--   abraham and grover are toy siblings

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
with
  stack(name, total_height, last_added, amount) as (
    select name, size, size, 1 from dogs_sizes union
    select a.name||", "||b.name, a.total_height+b.size, b.size, amount+1
      from stack as a, dogs_sizes as b
      where b.size>a.last_added and a.total_height<170 and amount<4
  )
  select name, total_height from stack 
    where total_height>=170 and amount=4 order by total_height;
-- Expected output:
--   abraham, delano, clinton, barack|171
--   grover, delano, clinton, barack|173
--   herbert, delano, clinton, barack|176
--   fillmore, delano, clinton, barack|177
--   eisenhower, delano, clinton, barack|180

-- All non-parent relations ordered by height difference
CREATE TABLE non_parents AS 
  WITH
    non_parents(ancestor, descendent) AS (
      SELECT a.parent, b.child FROM parents AS a, parents AS b
      WHERE a.child = b.parent UNION
    SELECT ancestor, child FROM non_parents, parents 
      WHERE parent = descendent
  )
  SELECT ancestor AS first, descendent AS second FROM non_parents;

CREATE TABLE no_order AS
  SELECT first as one, second as two FROM non_parents UNION
  SELECT second      , first         FROM non_parents;

SELECT a.one, a.two
  FROM no_order AS a, dogs as b, dogs as c
  WHERE a.one = b.name AND a.two = c.name  
  ORDER BY b.height - c.height;

-- Expected output:
--   fillmore|barack
--   eisenhower|barack
--   fillmore|clinton
--   eisenhower|clinton
--   eisenhower|delano
--   abraham|eisenhower
--   grover|eisenhower
--   herbert|eisenhower
--   herbert|fillmore
--   fillmore|herbert
--   eisenhower|herbert
--   eisenhower|grover
--   eisenhower|abraham
--   delano|eisenhower
--   clinton|eisenhower
--   clinton|fillmore
--   barack|eisenhower
--   barack|fillmore


