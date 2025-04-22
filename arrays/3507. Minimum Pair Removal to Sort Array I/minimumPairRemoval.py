class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        # Iterate while the array is not sorted
        while nums != sorted(nums):
            min_sum = float('inf')
            j = 0

            for i in range(len(nums) - 1):
                # Keep track of the pair with the min sum, and their sum
                # < ensures we keep the left most pair, if sums are equal
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    # Index of the first element in the pair
                    j = i
            
            # Replace the pair with their sum
            nums = nums[:j] + [min_sum] + nums[j+2:]
            # Keep track of how many times we replaced a pair with their sum
            count += 1
        
        return count