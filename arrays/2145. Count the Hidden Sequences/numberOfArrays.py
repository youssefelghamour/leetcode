class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int

        Finds the hidden sequence.
        differences is a list of numbers, each number is the difference between sequence numbers
        if the first sequence number is x (seq[0]), then the next number seq[1] = x + difference[0]
        
        The key is to find out the first number of the sequence, and we can build the sequence from differences:
        - We try all numbers between lower and upper, and create a sequence for each number
        - When the sequence is constructed, we check if it's lowest value is in range (>= lower)
        - We check the sequence's max number if it's in range (<= upper)
        - If both are in range, we have a valid sequence, we increase the count

        Ex: differences = [1,-3,4], lower = 1, upper = 6
        -> nums = [1, 2, 3, 4, 5, 6]: The potential numbers that could be the first num in the sequence
            - num = 1: sequence = [1]
                - i = 0: append to seq, last elem in seq + diff to add: 1 + diff[0] = 1 + 1 = 2, seq = [1, 2]
                - i = 1: append to seq, last elem in seq + diff to add: 2 + diff[1] = 2 - 3 = -1, seq = [1, 2, -1]
                - i = 2: append to seq, last elem in seq + diff to add: 1 + diff[2] = -1 + 4 = 3, seq = [1, 2, -1, 3]
                -> min(seq) = -2 < lower = 1, not a valid seq, don't count it
            ...
            - num = 3: sequence = [3]
                - i = 0: append to seq, last elem in seq + diff to add: 3 + diff[0] = 3 + 1 = 4, seq = [3, 4]
                - i = 1: append to seq, last elem in seq + diff to add: 2 + diff[1] = 4 - 3 = 1, seq = [3, 4, 1]
                - i = 2: append to seq, last elem in seq + diff to add: 1 + diff[2] = 1 + 4 = 5, seq = [3, 4, 1, 5]
                -> min(seq) = 1 = lower, & max(seq) = 5 < upper = 6 => valid seq, count += 1
            ...
        
        We keep track of min and max, to exit early if the sequence is not valid, we don't need to keep constucting it
        """
        """
        nums = [num for num in range(lower, upper + 1)]
        sequence = []
        # Counts the number of valid hidden sequences possible
        count = 0
        
        for num in nums:
            # Reset the sequence to start with a new number in the range lower to upper
            sequence = [num]
            min_val = num
            max_val = num

            for i in range(len(differences)):
                new_num = sequence[-1] + differences[i]
                sequence.append(new_num)

                # Track min and max as we go, to check the range early
                min_val = min(min_val, new_num)
                max_val = max(max_val, new_num)

                # Early exit if out of bounds
                if min_val < lower or max_val > upper:
                    break
            
            if min(sequence) >= lower and max(sequence) <= upper:
                count += 1
        
        return count
        """
        """
        count = 0

        for num in range(lower, upper + 1):
            min_val = num
            max_val = num

            for d in differences:
                num += d

                min_val = min(min_val, num)
                max_val = max(max_val, num)

                if min_val < lower or max_val > upper:
                    break
            
            if min_val >= lower and max_val <= upper:
                count += 1
        
        return count
        """
        num = lower
        min_val = lower
        max_val = lower
        for d in differences:
            num += d
            min_val = min(min_val, num)
            max_val = max(max_val, num)
        
        seq_range = max_val - min_val

        # Check if there's enough space in the range [lower, upper] to fit seq_range
        if upper - lower < seq_range:
            return 0

        return (upper + 1 - lower) - seq_range