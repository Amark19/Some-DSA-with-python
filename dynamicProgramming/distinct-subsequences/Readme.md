# Distinct Subsequences

## Recursion

Lets consider an example to understand the problem statement.
s = "babgbag", t = "bag" if u see carefully this problem also contains
a typical property of recursion where we either pick or not pick & infinite
supply problem.

- If char from s and t are equal,
  1. We search rest of t in rest of s i.e g is matched then we search bag in rest of s
  (take)
  2. Or Else search current char in rest of s
  3. Sum it up 1 + 2
- If char from s and t are not equal,
  1. Search current char in rest of s

## Tabulation