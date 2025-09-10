class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int

        Process:
            1. Find all blocked friendships: pairs of users who don’t share a language
            2. Collect all users from these blocked friendships
            3. Count how many of these users know each language
            4. The most common language among them is the one you’ll teach
            5. Teach it to every user in blocked friendships who doesn’t already know it
            6. Return the number of users taught
        """
        # Users in a friendship that can't communicate to each other
        blocked_users = set() # Don't add duplicate users
        # Key: language, value: set of user who speak it
        common_languages= {}
        # The most common language among blocked users (key in common_languages dict)
        most_common_lang = None
        # The number of blocked users who speak the most common language
        max_count = 0
        result = 0

        for f in friendships:
            u = f[0]
            v = f[1]

            # Check if the friendship is blocked
            blocked = True
            # Users are 1 indexed while languages array is 0 indexed
            for l in languages[u - 1]:
                # If they share just one language
                if l in languages[v - 1]:
                    # They can communicate
                    blocked = False
                    break
            
            if blocked:
                blocked_users.add(u)
                blocked_users.add(v)
        
        # Populate the common languages dict
        for user in blocked_users:
            for language in languages[user - 1]:
                if language not in common_languages:
                    common_languages[language] = set()
                common_languages[language].add(user)
        
        # Find the most common language among blocked users
        for lang, users in common_languages.items():
            if len(users) > max_count:
                max_count = len(users)
                most_common_lang = lang

        # Count the number of blocked users who need to learn the  most common language
        # result = len(blocked_users) - len(common_languages[most_common_lang])
        for u in blocked_users:
            if u not in common_languages[most_common_lang]:
                result += 1
        
        return result