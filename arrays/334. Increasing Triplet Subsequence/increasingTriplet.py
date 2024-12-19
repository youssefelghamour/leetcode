class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')  # Smallest value
        b = float('inf')  # Second smallest value

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True  
        
        return False