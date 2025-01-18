class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, stack = [], []
        
        
        def backtrack(start):
            result.append(stack[:])
            for i in range(start, len(nums)):
                stack.append(nums[i])
                backtrack(i + 1)
                stack.pop()

                
        backtrack(0)
        
        return result