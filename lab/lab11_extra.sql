-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

-- Lengths of possible paths between two states that enter only
-- landlocked states along the way.
create table inland_distances as
  with
    inland(start, end, hops) as (
      select state, state, 0 from landlocked union
      select start, s2, hops + 1
        from inland, adjacencies, landlocked
        where end = s1 and s2 = state and hops < 8
    )
  select s1 as start, s2 as end, 2 as hops from adjacencies union
  select start.s1 as start, end.s2 as end, hops+2 as hops
    from adjacencies as start, adjacencies as end, inland
    where start.s2 = start and end.s1 = end;

select "Lengths of inland paths between CA and WA:";
select * from inland_distances where start = "CA" and end = "WA" order by hops;

select "States 2 inland hops from CA:";
select end from inland_distances where start = "CA" and hops = 2;
