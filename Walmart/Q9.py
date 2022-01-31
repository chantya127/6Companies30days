
# Question : Guess Number Higher or Lower II

# Input: n = 10
# Output: 16
# Explanation: The winning strategy is as follows:
# - The range is [1,10]. Guess 7.
#     - If this is my number, your total is $0. Otherwise, you pay $7.
#     - If my number is higher, the range is [8,10]. Guess 9.
#         - If this is my number, your total is $7. Otherwise, you pay $9.
#         - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
#         - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
#     - If my number is lower, the range is [1,6]. Guess 3.
#         - If this is my number, your total is $7. Otherwise, you pay $3.
#         - If my number is higher, the range is [4,6]. Guess 5.
#             - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
#             - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
#             - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
#         - If my number is lower, the range is [1,2]. Guess 1.
#             - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
#             - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
# The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.


# Approach :  As the number will be in between 1 to n , so apply dp approach
# at each iteration 'i' , the cost of the operation is i and find the minimum one from it.

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        def solve(low , high):
            
            if (low >= high):
                return 0
            
            if (dp[low][high] != -1):
                return dp[low][high]
            
            maxi = float('inf')
            
            for i in range(low , high+1,1):
                
                val = max(solve(low , i-1) , solve(i+1 , high)) + i
                
                maxi = min(maxi , val)
            
            dp[low][high] = (maxi)
            return dp[low][high]
        
        dp = [[-1 for _ in range(n+1)]for _ in range(n+1)]
        return solve(1,n)

if __name__ == '__main__':

    n = 10
    obj = Solution()
    ans = obj.getMoneyAmount(n)
    print(ans)