# Question : Given a set of N nuts of different sizes and N bolts of different sizes. There is a one-one mapping between nuts and bolts.
#  Match nuts and bolts efficiently.


# Input: N = 5  nuts[] = {@, %, $, #, ^} bolts[] = {%, @, #, $ ^}

# Output: 
# # $ % @ ^
# # $ % @ ^

# Approach : Just sort both the arrays

class Solution:

    def solve(self , nuts ,bolts):
        nuts.sort()
        bolts.sort()

    
    nuts = {'@', '%', '$', '#',' ^'}
    bolts = {'%', '@', '#', '$', '^'}

    obj = Solution()
    ans = obj.maxProfit(nuts ,bolts)
    print(bolts)
    print(nuts)