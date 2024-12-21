class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            """ Rearrange the list putting each num at index num - 1
                ex: value 2 at index 1 : nums[i] = 2 is moved to index = nums[i] - 1 = 1
                    value 3 at index 2 : nums[i] = 3 is moved to index = nums[i] - 1 = 2
            """
            # The missing number inside the list can't be > n (case where nums has numbers from 1 to n)
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        print(nums)
        
        for i in range(n):
            """ If the number is not wher it's supposed to be
                ex: nums[0] = 2 found at index 0 when it should be at index 1,
                    meaning that i + 1 = 1 is missing
            """
            if nums[i] != i + 1:
                # Return the missing element
                return i + 1
        
        # If all numbers from 1 to n are present in the list, the missing number will be n+1
        return n + 1