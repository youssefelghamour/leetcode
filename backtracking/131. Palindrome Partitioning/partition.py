class Solution(object):
    def is_palindrome(self, s):
        """ Checks if a string is palindrome
        :type s: str
        :rtype: Boolean
        """
        if not s:
            return False
        for i in range(0, len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []

        def backtrack(start, path):
            if start == len(s):  # If we've reached the end of the string
                result.append(path[:])  # Append the current partition to result
                return
            
            for i in range(start, len(s)):
                substring = s[start:i+1]  # Get the current substring
                if self.is_palindrome(substring):
                    path.append(substring)  # Add the palindrome substring to path
                    backtrack(i + 1, path)  # Recurse for the next part of the string
                    path.pop()  # Remove the last substring to try other partitions

        backtrack(0, [])

        return result