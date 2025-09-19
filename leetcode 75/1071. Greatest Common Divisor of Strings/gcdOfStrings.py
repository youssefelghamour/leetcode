class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        min_len = min(len(str1), len(str2))

        # Find the min number that divides both lengths (start from 1 to get the smallest substring)
        for i in range(min_len + 1, 0, -1):
            if (len(str1) % i == 0) and (len(str2) % i == 0):
                # Check if the substring makes both strings
                substring = str1[:i]

                # i divides each string into a number of substrings
                num1 = len(str1) // i
                num2 = len(str2) // i

                # Check if multiplying the substring by that number gives the actual whole string
                if (substring * num1 == str1) and (substring * num2 == str2):
                    return substring
                else:
                    continue
        
        return ""