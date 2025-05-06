class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        
        Both players can keep choosing 1 on every turn
        The player who loses is the one who ends up with the 1 at the end,
        and won't have a number to choose, since x has to be > 0 and < n = 1

        - So if n is even, Alice will choose first, 1, n - 1 will be odd
          Bob gets an odd number always from Alice, that means he's the one who'll end up with 1 (odd number)
        - If the n is odd, Alice starts with an odd, gives an even to Rob
          that means Alice is the one who'll end up with 1 (odd number)
        
        -> start with odd, lose; start with even win

        -> n = 5, odd = bob wins
        1 2 3 4 5  a chooses 1
        1 2 3 4    b chooses 1
        1 2 3      a chooses 1
        1 2        b chooses 1
        1          a loses, has no more choices

        -> n = 4, even = alice wins
        1 2 3 4    a chooses 1
        1 2 3      b chooses 1
        1 2        a chooses 1
        1          b loses, has no more choices
        """
        return n % 2 == 0