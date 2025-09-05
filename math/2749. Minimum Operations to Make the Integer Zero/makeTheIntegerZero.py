class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        """
        Greedy process: Impossible doesn't work always skips a valid i
        1. Start with the largest possible i (60) and work down to 0
            - if we start from 0 we're gonna get the max number of operations
            - starting from 60 makes sure we substract the biggest number possible each time
              thus finding the min number of operations
        2. For each i, subtract 2**i + num2 from num1 as many times as possible
            - if substracting makes num1 negative then i is too big dercrease it until num1 is positive or zero
        3. If num1 becomes negative, decrease i and continue
        4. Repeat until either num1 reaches exactly 0 (success) or i = 0 and num1 != 0 (impossible)
        5. Return the total number of operations performed, or -1 if impossible
        
        operations = 0
        temp = num1
        
        for i in range(60, -1, -1):
            # substracting a negative number won't decrese num1 it'll increase it
            # breaks code and goes into an infinite loop
            if 2**i + num2 <= 0:
                continue

            temp -= 2**i + num2

            if temp < 0:
                temp = num1
                continue
            elif temp > 0:
                operations += 1

                # Process the same i as many times as possible
                while temp - (2**i + num2) >= 0:
                    temp -= 2**i + num2
                    operations += 1

                if temp == 0:
                    return operations

                num1 = temp
            else:
                operations += 1
                return operations
        
        return operations if num1 == 0 else -1
        """

        """
        suppose it takes us k operations for a certain num1 that means:
            - we substracted num2 a total of k times
            - and we substracted k different powers of 2
        -> operations = (k * num2) + (sum of k powers of 2)
        the final num1 = num1 - ((k * num2) + (sum of k powers of 2))
        our goal is for the_final_num1 = 0
        num1 - (k * num2) - (sum of k powers of 2) = 0
        num1 - (k * num2) =  sum of k powers of 2

        The goal here is to find x = num1 - (k * num2) such that x can be written as the sum of exactly k powers of 2
        If such an x exists, then k is the number of operations, so:
            1. pick a candidate k (number of operations)
            2. calculate x = num1 - k * num2
            3. check if x can be expressed as a sum of exactly k powers of 2
                a number x can be written as a sum of k powers of 2 if:
                    - number of 1s in the binary representaion of x: bin(x).count('1') <= k
                        it's the min num of powers of 2 needed to make x (each 1 is a distinct power)
                        so if it's <= k we can split the rest the other powers to get to k
                    - k <= x (when we hit a k > x we stop it's impossible)
                        the sum of k powers is always at least k (k * 2**0 = k, if k > 0 it can't be = x)

        example: num1 = 3, num 2 = -2
            - k = 1: x = 3 - 1*(-2) = 5, can't be made into the sum of the powers of 2: not a power of 2
            - k = 2: x = 7, in binary 111 (4 + 2 + 1) which is the sum of 3 powers of NOT 2. so k = 2 is wrong
                bin(7).count('1') = 3 > k
            - k = 3: x = 9, 1001, bin(9).count('1') = 2 < k = 3 and 3 < 9, so k is our answer
        """

        k = 1

        while True:
            x = num1 - k * num2

            # Check the two conditions
            # to see if the current x with this specific k can be written as the sum of k powers of 2
            if k > x:
                return -1
            if bin(x).count('1') <= k:
                return k
            
            k += 1