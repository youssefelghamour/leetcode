class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int

        Process:
        - Whoever picks the last flower wins
        - Since Alice picks first, the sum x+y determines who takes the last flower:
            - If x + y is odd, Alice takes the last flower -> she wins
            - If x + y is even, Bob takes the last flower -> Alice loses
        - We need to count all (x,y) pairs with odd sum

        - count how many numbers are odd and even in [1, n] and [1, m], then use combinatorics:
            - odd + even -> sum is odd
            - even + odd -> sum is odd
            -> Result would be: (odds_in_x * evens_in_y) + (evens_in_x * odds_in_y)
        
        example: n = 3, m = 2:
            - x numbers are [1, 2, 3]
                - odds = [1, 3] -> 2 numbers
                - evens = [2] -> 1 number
            - y numbers 1 to m are [1, 2]
                - odds = [1] -> 1 number
                - evens = [2] -> 1 number
            - For the sum x + y to be odd:
                - case 1: x odd, y even -> pairs = odds_in_x * evens_in_y = 2 * 1 = 2
                - case 2: x even, y odd -> pairs = evens_in_x * odds_in_y = 1 * 1 = 1
            - Total pairs = 2 + 1 = 3
        """
        odds_in_x = 0
        evens_in_x = 0
        odds_in_y = 0
        evens_in_y = 0

        """ Too slow
        for x in range(n):
            for y in range(m):
                if (x + y) % 2 != 0:
                    result += 1
        """

        """ Works but can be improved
        for x in range(n):
            if x % 2 == 0:
                evens_in_x += 1
            else:
                odds_in_x += 1
        
        for y in range(m):
            if y % 2 == 0:
                evens_in_y += 1
            else:
                odds_in_y += 1
        
        return (odds_in_x * evens_in_y) + (evens_in_x * odds_in_y)
        """

        """
        To make it faster:
        For n = 5 -> numbers 1 2 3 4 5 -> odd, even, odd, even, odd -> odds = 3, evens = 2
            - n // 2 counts complete pairs -> each pair (1,2), (3,4) has 1 odd + 1 even -> 5//2 = 2 -> 2 odds, 2 evens
            - n % 2 checks extra number -> 5%2 = 1 -> extra odd
        So odds = 2 + 1 = 3, evens = 2. Counts odds/evens without loops
        -> odds = (from pairs) + (extra) = n // 2 + n % 2 = 2 + 1 = 3
        -> evens = (from pairs) = n // 2 = 2
        """
        odds_in_x = n // 2 + n % 2
        evens_in_x = n // 2
        odds_in_y = m // 2 + m % 2
        evens_in_y = m // 2
        
        return (odds_in_x * evens_in_y) + (evens_in_x * odds_in_y)