class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mod = 10**9 + 7
        total = 0
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                # Each element between left & right has two possibilities: included or not (2)
                # in the subsequence, the number of subsequences including nums[left] would be
                # 2**(the number of elements)
                # total = (total + (2**(right - left)) % mod) % mod # Very slow
                total = (total + pow(2, right - left, mod)) % mod
                left += 1
            else:
                right -= 1
        
        return total