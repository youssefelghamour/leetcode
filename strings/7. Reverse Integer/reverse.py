class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        num = list(str(abs(x)))
        
        for i in range(len(num) // 2):
            temp = num[i]
            num[i] = num[len(num) - 1 - i]
            num[len(num) - 1 - i] = temp
        
        result = int("".join(num))
        
        if result > 2**31 - 1 or result < -2**31:
            return 0
            
        return -result if is_negative else result