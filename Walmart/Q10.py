
# Question : Generate Random Point in a Circle


#Input
# ["Solution", "randPoint", "randPoint", "randPoint"]
# [[1.0, 0.0, 0.0], [], [], []]
# Output
# [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]

# Explanation
# Solution solution = new Solution(1.0, 0.0, 0.0);
# solution.randPoint(); // return [-0.02493, -0.38077]
# solution.randPoint(); // return [0.82314, 0.38945]
# solution.randPoint(); // return [0.36572, 0.17248]


# Approach : Go on generating uniformly random pt,such that a**2+b**c <= r**2

import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        while True:
            a,b = random.uniform(-self.r , self.r) , random.uniform(-self.r , self.r)
            if a**2 + b**2 <= (self.r)**2:
                return [a+self.x ,b+self.y]

if __name__ == '__main__':

    pass