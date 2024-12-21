class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1