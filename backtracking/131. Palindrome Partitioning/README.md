# 131. Palindrome Partitioning

Given a string `s`, partition `s` such that every **substring** of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.


## Example 1:

- Input: s = "aab"
- Output: [["a","a","b"],["aa","b"]]

## Example 2:

- Input: s = "a"
- Output: [["a"]]
 

## Constraints:

- 1 <= s.length <= 16
- s contains only lowercase English letters.

## Process:

```
Start with path = [], start = 0

Loop from i = 0:
- s[0:1] = "a" → palindrome → path = ["a"]
    backtrack(1)

    Loop from i = 1:
    - s[1:2] = "a" → palindrome → path = ["a", "a"]
        backtrack(2)

        Loop from i = 2:
        - s[2:3] = "b" → palindrome → path = ["a", "a", "b"]
            backtrack(3) → END → save ["a", "a", "b"]
        backtrack → path = ["a", "a"]
        - i = 2 done
    - s[1:3] = "ab" → NOT palindrome → skip
    backtrack → path = ["a"]
- s[0:2] = "aa" → palindrome → path = ["aa"]
    backtrack(2)

    Loop from i = 2:
    - s[2:3] = "b" → palindrome → path = ["aa", "b"]
        backtrack(3) → END → save ["aa", "b"]
    backtrack → path = ["aa"]
- s[0:3] = "aab" → NOT palindrome → skip

Result: [["a", "a", "b"], ["aa", "b"]]
```

```
             []
            /   \
        ["a"]   ["aa"]
         /         \
    ["a","a"]    ["aa","b"]
        |
    ["a","a","b"]
```