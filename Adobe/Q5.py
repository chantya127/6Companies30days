# Question :Given two numbers n and x, find out the total number of ways 
# in can be expressed as sum of xth power of unique natural numbers.


# Input: n = 100, x = 2
# Output: 3
# Explanation: 100 = 102 
# 62 + 82 and 12 + 32 + 42 + 52 + 72 
# Hence total 3 possibilities. 

# Approach : The last number i.e limit will be upto nth root of n.
# then any number will have choice whether to get included or not.

class Solution:
    def numOfWays(self, n, x):
        # code here
        
        def solve(curr,last):
            
            if (curr == n):
                return 1
            
            if (curr > n or last >limit):
                return 0
            
            if (dp[curr][last] != -1):
                return dp[curr][last]
                
            power = last**x
            
            count = solve(curr +power , last+1)
            count += solve(curr , last+1)
            
            dp[curr][last]  = count
            return dp[curr][last]
        
        limit = int(n**(1/x))+1
        
        ans = 0
        
        dp = [[-1 for _ in range(limit+1)]  for _ in range(n)]
        ans = solve(0,1)
        return (ans)
        

if __name__ == '__main__':

    x = 2
    n = 100
    obj = Solution()
    ans = obj.numOfWays(n,x)
    
    print(ans)