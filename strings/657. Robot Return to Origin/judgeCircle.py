class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0

        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y += 1
            else:
                y -= 1
        
        return x == 0 and y == 0