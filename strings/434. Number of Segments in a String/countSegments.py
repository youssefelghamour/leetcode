class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segments = 0
        b = 0  # Track the beginning of each word

        if not s:
            return 0
        
        for i in range(len(s)):
            if s[i] == " ":
                if i > b:
                    segments += 1
                b = i + 1  # Skip space

        # Add the last word
        if b != len(s):  # There could still be a word after the last space
            segments += 1

        return segments