class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int

        - start altitude always = 0
        - altitude at i+1 = previous altitude (alt[i]) + gain[i]
        """
        """ Makes a list -> O(n) space complexity
        alt = []
        alt.append(0)

        for i in range(len(gain)):
            alt.append(gain[i] + alt[i])
        return max(alt)
        """
        max_alt = 0
        prev_alt = 0
        for i in range(len(gain)):
            current_alt = prev_alt + gain[i]
            max_alt = max(max_alt, current_alt)
            prev_alt = current_alt
        return max_alt