# Wildcard matching

## Approach

1. Like all string matching algorithms, here if two chars are equal we move to next char in both strings.
2. If we encounter a `?` in pattern, we move to next char in both strings.
3. If string has `*` we have two options:
   1. We can ignore `*` and move to next char in string. (empty string)
   2. We can ignore current char in string and move to next char in pattern.
   3. Why can't we return True if "*" is present ?
      - Let's suppose we have strings s = `geeks` and p =`f*ks`
      - If we match entire `gee` with `*` starting from end then we will have `f` left in pattern. 
      - That remain unmatched.