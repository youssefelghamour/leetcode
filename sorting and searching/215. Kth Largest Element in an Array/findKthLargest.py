class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = sorted(nums, reverse=True)
        
        return lst[k - 1]