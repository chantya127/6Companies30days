# Question :Given an integer array arr of size N, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum and find the minimum difference

# Input: Input: N = 4, arr[] = {1, 6, 11, 5} 
# Output: 1
# Explanation: 
# Subset1 = {1, 5, 6}, sum of Subset1 = 12 
# Subset2 = {11}, sum of Subset2 = 11 

# Approach : Use knapsack pattern and find all the subsets possible.
# then take the subsets which is maximum possible and subtract from whole sum of the array.
class Solution:
    def minDifference(self, arr, n):
        # code here
        
        summe = sum(arr)
        dp = [[False for _ in range(summe+1)] for _ in range(n+1)]
        
        for row in range(n+1):
            dp[row][0] = True
           
        for row in range(1,n+1):
            for col in range(1,summe+1):
                
                if (col >= arr[row-1]):
                    
                    dp[row][col] = dp[row-1][col] or dp[row-1][col-arr[row-1]]
                
                else:
                    dp[row][col] = dp[row-1][col]
                    
        poss= []
        for col in range(summe//2+1):
            if (dp[n][col]):
                poss.append(col)
        
        ans = float('inf')
# 		print(poss)
        for num in poss:
            
            diff = summe - 2*num
            if (diff >=0):
                ans = min(ans , diff)
               
        return ans

if __name__ == '__main__':

    
    N = 4
    A = [1, 6, 11, 5]

    obj = Solution()
    ans = obj.minDifference(A , N)
    print(ans)