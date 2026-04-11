class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]

            make a stack and add to it the first element
            iterate over asteroids
            compare each element with the top element in the stack
            if collision
                if stack bigger -> don't add move on
                if asteroid bigger -> while it's bigger
                    pop stack
                    after loop
                        -> if stack empty or ther's no collision -> add curr asteroid
                        -> if both equal -> pop stack, don't add
                        -> if the stack's asteroid is bigger -> don't add
                both equal -> pop stack and move on
            no collision -> add asteroid
        """
        stack = []
        stack.append(asteroids[0])

        for i in range(1, len(asteroids)):
            # Collision
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                # both equal -> both get destroyed -> pop stack and move on
                if stack[-1] == - asteroids[i]:
                    stack.pop()
                    continue
                # if the current asteroid is bigger
                elif stack[-1] > 0 and asteroids[i] < 0:
                    # While it's bigger and there's a collision -> asteroids in stack get destroyed
                    while stack and stack[-1] > 0 and asteroids[i] < 0 and stack[-1] < abs(asteroids[i]):
                        stack.pop()
                    # If after the loop the asteroidin the stack is bigger -> current asteroid gets destroyed
                    if stack and stack[-1] > abs(asteroids[i]):
                        continue
                    # If both equal -> both get destroyed -> pop stack and move on
                    elif stack and stack[-1] == abs(asteroids[i]):
                        stack.pop()
                        continue
                    # If stack is empty or there's no collisions anymore -> add the current asteroid
                    else:
                        stack.append(asteroids[i])
            # No Collision -> add current asteroid
            else:
                stack.append(asteroids[i])

        return stack