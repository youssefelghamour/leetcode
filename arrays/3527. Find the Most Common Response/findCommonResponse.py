class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        occurrences = {}  # key = responses[i], value = its occurrence
        max_occurrence = 0
        result = ""

        for i in range(len(responses)):
            # Turn into a set to remove duplicates
            day_responses = set(responses[i])

            # Count the occurence of each response in the dict
            for resp in day_responses:
                if resp in occurrences:
                    occurrences[resp] += 1
                else:
                    occurrences[resp] = 1
        
        # Find the max occurrence
        max_occurrence = max(v for v in occurrences.values())

        temp = []
        # Gather the responses that have the same max_occurrence value
        temp = [resp for resp in occurrences.keys() if occurrences[resp] == max_occurrence]

        # Find the lexicographically smallest response
        result = min(temp)
        
        return result