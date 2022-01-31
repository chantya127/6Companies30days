# Question :Given a A X B matrix with your initial position at the top-left cell, find the number of possible unique paths to reach the bottom-right cell of the matrix from the initial position.



# Input:
# A = 3, B = 4
# Output: 10
# Explanation: There are only 10 unique
# paths to reach the end of the matrix of
# size two from the starting cell of the
# matrix.


# Approach :Maintain a 2d dp matrix where state of dp[i][j] = dp[i-1][j] + dp[i][j-1]
# stating that ,for reaching each index we have two choices


class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,nr, nc):
        #code here
        grid = [[0 for _ in range(nc+1)]for _ in range(nr+1)]
        for i in range(nr):
            grid[i][0] = 1
        for j in range(nc):
            grid[0][j] = 1
            
        for i in range(1,nr):
            for j in range(1, nc):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return(grid[nr-1][nc-1])
        


if __name__ == '__main__':

    r = 3;c = 4
    obj = Solution()
    ans = obj.NumberOfPaths(r,c)
    print(ans)