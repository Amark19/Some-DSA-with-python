# Dynamic Programming

## Recursion

- Base case ( will be the smallest possible input)
- Analyze the pattern by taking the smallest possible input
- Reduce the problem to the smallest possible input

## Memoization (Top Down)

- Find changing parameters
- Initialize a memoization array with -1
- Check if the value is already calculated
- If not calculated, calculate and store it in the memoization array

## Tabulation (Bottom Up)

- From recursive base case, analyze the base case and fill 
the smallest possible input with known outcomes.
- Write loops for changing parameters and fill the table
- Return the last value of the table