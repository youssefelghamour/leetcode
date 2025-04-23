class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dict having sum of digits as key, and a list of the numbers who's sum of digits equals this sum
        # { a+b: [ab, ba], a: [a0, a] }
        sums = {}
        # The number of groups that have the largest size
        count = 0

        # From 1 to n
        for i in range(1, n + 1):
            # Sum the digits of the number
            digit_sum = sum(int(digit) for digit in str(i))

            if digit_sum in sums:
                # Add the number to the group of this sum
                sums[digit_sum].append(i)
            else:
                # Initialize a new list for this sum
                sums[digit_sum] = [i]
        
        # Find the biggest group of numbers that give the same sum
        max_size = max(len(v) for v in sums.values())
        
        # Count how many max groups have the same size
        for v in sums.values():
            if len(v) == max_size:
                count += 1
        
        return count