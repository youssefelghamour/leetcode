class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        # dictionary to store num, index pairs: {nums[i]: i} 
        visited = {}
        
        for i in range (len(nums)):
            if target - nums[i] in visited:
                    result = [i , visited[target - nums[i]]]
            
            visited[nums[i]] = i
        
        return result