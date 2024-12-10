class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters to lowercase
        cleaned_s = ''.join([char.lower() for char in s if char.isalnum()])
        reverse_s = cleaned_s[::-1]
        return cleaned_s == reverse_s