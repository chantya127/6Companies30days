
# Question : Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4


# Approach :Use BFS approach and start with all the rotten oranges with time 0
# finally check if some fresh oranges are left or not.

from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        
        ququ = deque()
        fresh = 0
        
        row_size,col_size = len(grid), len(grid[0])
        
        for r in range(row_size):
            for c in range(col_size):
                
                if (grid[r][c] == 1):
                    fresh +=1
                
                elif(grid[r][c] == 2):
                    ququ.append((r,c))
        
        time = 0
        dirs = [(-1,0) ,(1,0) , (0,-1) , (0,1)]
        
        while(ququ and fresh>0):
            
            time +=1
            size = len(ququ)
            
            for _ in range(size):
                
                r,c = ququ.popleft()
                for (a,b) in dirs:
                    nrow,ncol = r+a , c+b
                    
                    if (0 <= nrow <row_size and 0 <= ncol <col_size and grid[nrow][ncol] == 1):
                        fresh -=1
                        grid[nrow][ncol] = 2
                        
                        ququ.append((nrow,ncol))
        
        if (fresh ==0):
            return (time)
        
        else:
            return -1

if __name__ == '__main__':

    grid = [[2,1,1],[1,1,0],[0,1,1]]
    obj = Solution()
    ans = obj.orangesRotting(grid)
    print(ans)