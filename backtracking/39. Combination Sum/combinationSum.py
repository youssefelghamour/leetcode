class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

                                        []
                          _______________|_____________
                         |               |      |      |
                         2               3      6      7
                     ____|_____       ___|__
                    |          |     |      |
                    2,2       2,3    3,3   `3,6`   same here (2,6 - 2,2,6 - 3,3,3 - 3,6 - 6,6)
                 ____|____     |             
                |         |  `2,3,3`  exceeds target -> pop twice -> go back to 2
                2,2,2   2,2,3
               __|           
              |
            `2,2,2,2`   if the combinations is sorted and we return when we exceed target instead of continue:
                            from here we pop twice on the check and recursion straight back to 2,2
                            since we don't need to try any combination with 2,2,2 because adding the
                            even smallest element (2) makes us exceed the target
                        if we use continue
                            we'll be checking all possible combinations: 2,2,2,3 - 2,2,2,6 - 2,2,2,7
                            then when the loop ends we'll pop twice and go back to 2,2
        """
        result = []
        stack = []

        candidates.sort()
        
        def backtrack(start):
            # To see the whole tree without the exceeding subarrays print(stack)
            if sum(stack) == target:
                result.append(stack[:])
                return  # If we found 2,2,3 = target, no need to try 2,2,3,3 (same for 7 -> 7,7)

            for i in range(start, len(candidates)):
                stack.append(candidates[i])
                # To see the whole tree print(stack)
                if sum(stack) > target:
                    # To see the combinations we didn't choose & stopped at print(stack)
                    stack.pop()
                    return # If we don't want to explore further combinations like 2,2,2,3 (if the arr is sorted)
                    # continue # In case the array isn't sorted and we need to explore all combinations
                backtrack(i)
                stack.pop()
        
        backtrack(0)

        return result