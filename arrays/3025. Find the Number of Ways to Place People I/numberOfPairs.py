class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int

        Conditions:
        - A is on the upper left side of B:
            - Rectangle: A.x < B.x and A.y > B.y
            - Line: (A.x == B.x and A.y > B.y) or (A.y == B.y and A.x < B.x)
        - There are no other points in the rectangle (or line) they make (including the border):
            - means there is no point P where: A.x <= P.x <= B.x and A.y >= P.y >= B.y
        """
        result = 0
        
        # For every A in points find a B that makes a rectangle respecting the conditions
        for A in points:
            Ax = A[0]
            Ay = A[1]
            for B in points:
                Bx = B[0]
                By = B[1]

                # Rectangle or line
                if (Ax < Bx and Ay > By) or (Ax == Bx and Ay > By) or (Ay == By and Ax < Bx):
                    # Flag that marks the rectangle as valid
                    # A rectangle is invalid if it contains even 1 point inside it
                    valid = True

                    # Make sure there is no point inside the rectangle
                    for P in points:
                        Px = P[0]
                        Py = P[1]

                        # Ignore A and B
                        if P == A or P == B:
                            continue
                        
                        if Ax <= Px <= Bx and Ay >= Py >= By:
                            valid = False
                            break
                    
                    if valid:
                        result += 1
        
        return result