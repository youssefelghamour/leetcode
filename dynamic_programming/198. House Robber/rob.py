class Solution:
    def rob(self, nums: List[int]) -> int:
        """ prev1: Keeps track of the maximum money robbed up to the previous house
            prev2: Keeps track of the maximum money robbed up to two houses ago
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prev1 = nums[0]  # Robbing the first house
        prev2 = max(nums[0], nums[1])  # Robbing the max of first two houses
        
        for i in range(2, len(nums)):
            current = max(nums[i] + prev1, prev2)  # Rob this house or skip it
            prev1 = prev2  # Move to the next house
            prev2 = current
        
        return prev2