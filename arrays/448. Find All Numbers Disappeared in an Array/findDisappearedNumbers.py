class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = []
        i = 0
        j = 1
        n = len(nums)
        
        nums.sort()

        while j <= n:
            if i < n and nums[i] == j:
                while i < n and nums[i] == j:  # Skip all duplicates of j
                    i += 1
                j += 1
            else:
                missing.append(j)
                j += 1
        
        return missing