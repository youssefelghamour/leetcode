class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int

        Counts how many rabbits gave the same answer:
        - Each rabbit saying a number (ex: 2) means there are a group of rabbits of that color (2 + 1 = 3 in total)
        
        - We track how many rabbits we have seen for each answer (for 2 we're expecting the total 3)

        - If too many rabbits show up for one color (more than allowed in the group),
          we start a new group for that color, that means it's a new color group
            ex: [2, 2, 2, 2] first 3 rabbits say me and 2 others, so they're included in the same group of 3 rabbits
                but the fourth one isn't, it's occurrence will be the fourth > 3, so we add it to a new group
                groups[2] was 3: sum of three rabbits, so after adding this new group (fourth rabbit plus 2 other),
                groups[2] will become 6. and reset occurence[2] to 1 to count for the new group

        - At the end, we add up the sizes of all the groups to get the total rabbits
        """
        # Groups the groups of rabbits who gave the same answer/ who have the same color
        groups = {}
        # Counts the occurence of rabbits that gave the same answer
        occurrence = {}

        for a in answers:
            if a not in groups:
                # Add the rabbit that answerd + the number it gave
                groups[a] = 1 + a
                # First rabbit in this group of color
                occurrence[a] = 1
            else:
                # Increment the occurence within the same group (another rabbit with the same color)
                occurrence[a] += 1

                # If we have found all the rabbit with the same color
                # [2, 2, 2, 2, ...] this rabbit is a new color, since the first group of 3 rabbits is full groups[2] = 3
                # occurrence[2] will be 4 > 3 (2 + 1)
                if occurrence[a] > a + 1:
                    # Start a new count for the new group
                    occurrence[a] = 1
                    # Start a new group
                    groups[a] += a + 1
        
        return sum(groups.values())