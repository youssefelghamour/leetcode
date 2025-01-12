class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
        """
        n = len(nums)     
        # Formula calculates the sum of all numbers from 0 to n
        # Example: For n = 3, sum = 0 + 1 + 2 + 3 = 6
        # result will then be the sum of numbers of the list [0,...,n]
        result = (n * (n+1)) // 2
        for i in range(len(nums)):
            result -= nums[i]
        # Substracting the values from nums will leave us with the missing number
        # Same as doing: return result - sum(nums) instead of the loop
        return result