class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Process: We keep track of the streaks
        each time we find a new 0 we count it +1 and we see how many combinations it can have with current streak

        example: [0, 0, 0, 0, 1, 4, ...]
        - i = 3: streak = [0, 0, 0], we add nums[3] = 0
            - nums[3] counts as one combination [0] but it can form more combinations with the streak:
                -> nums[2:3] = [0, 0], nums[1:3] = [0, 0, 0] and nums[0:3] = [0, 0, 0, 0]
                -> the number of combinations would be the number of elements the streak has (from i to 0) = len(streak)
            - the total number of the combinations would be the previous result + the new number
        """
        """
        # Works but slow
        # (no need to have streak as an array it can just be the length that increases by 1 for each new element added)
        result = 0
        streak = []

        for i in range(len(nums)):
            if nums[i] == 0:
                streak.append(nums[i])
                result += len(streak)
            else:
                streak = []
        
        return result
        """
        result = 0
        streak = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                streak += 1
                result += streak
            else:
                streak = 0
        
        return result