# Similar Problems

- Longest Common Substring
- Longest Palindromic Subsequence
- Minimum insertions to form a palindrome
- Minimum insertion & deletion to convert a string to another string

## Longest Common Substring

This is simple u straigtly ignore those chars which are not equal & if equal then add 1.

## Longest Pallindromic Subsequence


If u think, two strings are pallindrome only when their reverse is also equal.

So, ideally Longest common subsequence of s1 & reverse of s1 will give us the answer.
That means if string is "abac" & if we match it with reverse & apply LCS on it,
things should work.
abac & caba

## Minimum insertions to form a palindrome

This is very similar problem to Longest Pallindromic Subsequence.
Because if u think minimum insertions to form a palindrome is nothing but
how many chars u need to insert to make a string palindrome. And that we can achieve by first finding the longest pallindromic subsequence & then subtracting it from the length of the string.

## Minimum insertion & deletion to convert a string to another string

This is also similar to Longest Common Subsequence.
Where we can just find the LCS of two strings & then subtract it from the length of the string to get the answer.