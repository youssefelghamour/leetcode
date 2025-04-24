class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_distinct = len(set(nums))
        count = 0

        for i in range(len(nums)):
            temp = set()
            for j in range(i, len(nums)):
                temp.add(nums[j])
                if len(temp) == total_distinct:
                    count += 1
        
        return count