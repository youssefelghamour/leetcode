class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        # Search boundaries
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # Expand to find the range
                start = mid
                end = mid
                
                # Move to the left if the previous element is equal to the target
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                    
                # Move to the right if the next element is equal to the target
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                
                result = [start, end]
                
                # Exit loop once the range is found
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result