class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        i = 0

        while i < len(nums):
            # Start with the current number
            a = nums[i]

            # Continue while consecutive numbers are found
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            # If the current number is not the same as the start, it means we have a range
            # if a != b: we add "->b", otherwise we keep "a"
            if a != nums[i]:
                ranges.append(str(a) + "->" + str(nums[i]))
            else:
                ranges.append(str(a))
            
            i += 1
                    
        return ranges