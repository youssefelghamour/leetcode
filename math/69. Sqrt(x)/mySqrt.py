class Solution:
    def mySqrt(self, x: int) -> int:
        """ Function that uses Binary search to find sqrt(x) """
        l = 0
        r = x
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid**2 > x:
                # Search in left
                r = mid - 1
            elif mid**2 < x:
                # Search in right
                l = mid + 1
            else:
                # If mid^2 == x
                return mid
        
        return r # The rounded-down number (r < l, and r^2 <= x)