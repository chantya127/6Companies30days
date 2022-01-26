
# Question : As Far from Land as Possible

# Input: Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

# Approach :  Just apply a mutlisource bfs starting at all 1's and find the last level till the bfs goes.

from collections import defaultdict,deque

class Solution:
    def maxDistance(self, grid):
        
        size = len(grid)
        
        ququ = deque()
        
        for row in range(size):
            for col in range(size):
                if (grid[row][col] == 1):
                    ququ.append((row,col))
        
        if (len(ququ) == 0 or len(ququ) == size*size):
            return (-1)
        
        dis = 0
        dirs = [(-1,0),(1,0) , (0,-1) , (0,1)]
        
        while(ququ):
            
            length = len(ququ)
            flag = 0
            
            for _ in range(length):
                
                row,col = ququ.popleft()
                
                for (a,b) in dirs:
                    
                    nrow,ncol = row+a , col+b
                    
                    if (0 <= nrow<size and 0<=ncol<size and grid[nrow][ncol] == 0):
                        grid[nrow][ncol] = 1
                        ququ.append((nrow,ncol))
                        flag = 1
            
            if (flag == 0):
                break

            dis +=1
            
        return (dis)
if __name__ == '__main__':

    grid = [[1,0,1],[0,0,0],[1,0,1]]
    obj = Solution()
    ans = obj.maxDistance(grid)
    print(ans)
