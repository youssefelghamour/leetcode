class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = 0
        curr_sum = 0
        left = 0

        for right in range(len(s)):
            if s[right] in vowels:
                curr_sum += 1

            if right - left + 1 > k:  # window exceeded size k
                if s[left] in vowels:
                    curr_sum -= 1
                left += 1

            if right - left + 1 == k:  # window exactly size k
                result = max(result, curr_sum)

        return result