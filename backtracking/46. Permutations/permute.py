class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = []
        visited = []
        
        
        def backtrack():
            # Created a permutation with all the numbers from nums
            if len(stack) == len(nums):
                result.append(stack[:])
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    # Mark this number as used in the CURRENT stack
                    visited.append(i)
                    # Add the current number to the stack (building the current permutation)
                    stack.append(nums[i])
                    
                    # Recursively continue building the stack with the next or previous numbers
                    backtrack()
                    
                    # After we finish the recursion, backtrack by removing the last added number
                    # So we can explore a different path
                    stack.pop()
                    # Unmark this index, so it can be used in the next path
                    visited.remove(i)
        
        
        backtrack()
        
        return result