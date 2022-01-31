# Question :Given a number and its reverse. Find that number raised to the power of its own reverse.


# Input:
# N = 2
# Output: 4
# Explanation: The reverse of 2 is 2
# and after raising power of 2 by 2 
# we get 4 which gives remainder as 
# 4 by dividing 1000000007.

# Approach : Just use fast exp technique

mod = (10**9+ 7)
class Solution:
    #Complete this function
    def power(self,n,r):
        #Your code here
        
        def solve(num ,power,dp):
            
            if (power <=0):
                return 1
            
            if (power == 1):
                return (num)
            
            if (power in dp):
                return (dp[power])
                
            val = solve(num , power//2 , dp)
            val = (val*val)%mod
            
            if (power%2 == 1):
                
                val = (val *num)%mod
            
            dp[power] = val
            return (dp[power])
        
        dp = {}
        
        ans = solve(n,r,dp)
        
        return (ans)

if __name__ == '__main__':

    n,r = 2,4
    obj = Solution()
    ans = obj.power(n,r)
    
    print(ans)