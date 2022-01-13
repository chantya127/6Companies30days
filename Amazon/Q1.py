# Question :Given the stock prices of N days in an array A[ ] and a positive integer K, find out the maximum profit a person can make in at-most K transactions

# Input: K = 2, N = 6
# A = {10, 22, 5, 75, 65, 80}
# Output: 87
# Explaination: 
# 1st transaction: buy at 10 and sell at 22. 
# 2nd transaction : buy at 5 and sell at 80.

# Approach : Use dp Approach.At start user can only buy or leave as it is. On eventh day user can buy or leave.
# While on the odd day , user has two choices whether to sell or leave as it is.

class Solution:
    def maxProfit(self, k, n, arr):
        # code here
        
        dp = [0]*(2*k)
        
        for idx in range(2*k):
            
            if (idx%2 ==0):
                dp[idx] = float('-inf')
            
            else:
                dp[idx] = 0
        
        
        for stock in range(n):
            
            
            for idx in range(2*k):
                
                if (idx ==0):
                    dp[idx]=  max(dp[idx] , -arr[stock])
                
                # buy state
                elif (idx%2 ==0):
                    
                    dp[idx] = max(dp[idx] , dp[idx-1] -arr[stock])
                
                # sell state
                else:
                    dp[idx] = max(dp[idx] , dp[idx-1] +arr[stock])
        
        print(dp)
        return (dp[-1])

if __name__ == '__main__':

    
    K = 2
    N = 6
    A = [10, 22, 5, 75, 65, 80]

    obj = Solution()
    ans = obj.maxProfit(K,N,A)
    print(ans)