
# Question : Given a grid of dimension nxm containing 0s and 1s. Find the unit area of the largest region of 1s.
# Region of 1's is a group of 1's connected 8-directionally (horizontally, vertically, diagonally).


# Input:
# Input: grid = {{1,1,1,0},{0,0,1,0},{0,0,0,1}}
# Output: 5
# Explanation: The grid is-
# 1 1 1 0
# 0 0 1 0
# 0 0 0 1
# The largest region of 1's is colored
# in orange.


# Approach :  Use dfs and find all the ones connected in the current components.
# Finally return the largest area.




class Solution:

    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        #Code here
        
        def solve(r,c):
            
            if (r <0 or c <0 or r >= row or c >= col or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            count = 1
            
            for (a,b) in dirs:
                
                count += solve(r+a, c+b)
            
            return (count)
        
        dirs = [(-1,0),(1,0) ,(0,-1) ,(0,1) , (-1,-1) ,(1,-1) ,(1,1),(-1,1)]
        row, col = len(grid) , len(grid[0])
        
        ans = 0
        for r in range(row):
            for c in range(col):
                
                if(grid[r][c] == 1):
                    count = solve(r,c)
                    ans = max(ans ,count)
         
        return ans


if __name__ == '__main__':

    grid = [[1,1,1,0],[0,0,1,0],[0,0,0,1]]

    obj = Solution()
    ans = obj.findMaxArea(grid)
    print(ans)