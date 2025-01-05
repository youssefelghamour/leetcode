class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            # If the left half is sorted
            if nums[start] <= nums[mid]:
                # If target is in the left half
                if target >= nums[start] and target < nums[mid]:
                    # Search in the left half
                    end = mid - 1
                else:
                    # Search in the right half
                    start = mid + 1
            # If the right half is sorted      
            elif nums[mid] <= nums[end]:
                # If target is in the right half
                if target > nums[mid] and target <= nums[end]:
                    # Search in the right half
                    start = mid + 1
                else:
                    # Search in the left half
                    end = mid - 1
        
        return -1