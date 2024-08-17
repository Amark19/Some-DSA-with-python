# minimum-cost-for-cutting-cake-i

## Description
This question is clearly of partition DP

## Approach
at each cut u generate two more partitions (have two possible solutions)
that gives us a hint to break recursion into two

also think about all the possibilities
at very first u don't know which first cut will give u minimalcost ..
so lets try out all the possibilities

try cutting all rows -> capture minimum
try cutting all columns -> capture minimum

return minimum between the two


## Changing Params

a partition can be represent in 4 params
        col_st col_end    
row_st      |_|_|
row_end     |_|_|

So yes that is our chaning params (starti,endi,startj,endj)

## Base case
Base case is simple u can't cut anything if u only have one cell... 