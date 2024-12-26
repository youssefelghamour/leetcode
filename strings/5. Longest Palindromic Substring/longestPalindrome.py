class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        
        for i in range(len(s)):
            # For every element, check if it makes a palindrome with the rest of the string:
            # check substrings starting from i to the end
            for j in range(i, len(s)):
                # If a palindrome is found and it's longer than the current one
                if s[i:j + 1] == s[i:j + 1][::-1] and j + 1 - i > len(palindrome):
                    palindrome = s[i:j + 1]
        
        return palindrome