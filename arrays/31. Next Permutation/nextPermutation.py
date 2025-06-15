class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p = -1

        # Find the pivot index of the element to be swaped to get the next permutaion
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                p = i - 1
                break
        
        if p == -1:
            # No pivot was found, then the list is the highest permuation possible [3, 2, 1]
            # We return the list reversed, that'd be the next permutation (starting over)
            nums.reverse()
            return

        for i in range(len(nums) - 1, p, -1):
            if nums[i] > nums[p]:
                # Swap the pivot element with the first bigger element from the end
                nums[p], nums[i] = nums[i], nums[p]
                break
        
        # Sort the sublist after the pivot to reset it to the lowest order for the next permutation
        # nums[p+1:] = sorted(nums[p+1:])
        # This sublist will always be in descending order, so we can just reverse it because it's faster
        nums[p+1:] = reversed(nums[p+1:])