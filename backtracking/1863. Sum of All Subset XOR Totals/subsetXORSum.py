class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []

        def xor(arr):
            """ calculates the XOR total of the arr """
            s = 0
            for n in arr:
                s ^= n
            return s

        def backtrack(start):
            """ Creates all possible subsets of the array with bakctracking """
            # Calculate the XOR total of this current sub array
            result = xor(stack)
            
            for i in range(start, len(nums)):
                stack.append(nums[i])
                result += backtrack(i + 1)
                stack.pop()

            # return the total for this subset
            return result
        
        return backtrack(0)