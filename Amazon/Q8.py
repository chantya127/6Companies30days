
# Question : There are N stairs, and a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, 
# the person can reach the top (order does not matter).



# Input: N = 4
# Output: 3
# Explanation: You can reach 4th stair in
# 3 ways.
# 3 possible ways are:
# 1, 1, 1, 1
# 1, 1, 2
# 2, 2

     #  Examples
        # 1 -> 1
        # 2 -> 2
        # 3 -> 2
        # 4 -> 3
        # 5 -> 3
        # 6 -> 4
        # 7 -> 4
        # 8 -> 5

# Approach : just return (n//2)+1 , try out few examples to know about it


mod = 10**9+7

class Solution:

    def countWays(self,m):
        
        return 1 + m//2

if __name__ == '__main__':

    m =4
    obj = Solution()
    ans = obj.countWays(m)
    print(ans)