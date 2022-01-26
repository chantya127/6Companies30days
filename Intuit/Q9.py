
# Question : Pacific Atlantic Water Flow


#Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
#Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


# Approach : Maintain two grids , pacific and atlantic stating the points which can reach the resp river.
# apply dfs from all 4 sides . finally return the pts which are 1 at both pac and at.


class Solution:
    def pacificAtlantic(self, heights):
        
        def solve(row,col , matrix , prev):
            
            if (row<0 or row>=row_size or col<0 or col>=col_size or heights[row][col]<prev or matrix[row][col] == 1):
                return 
            
            matrix[row][col] = 1
            
            for (a,b) in dirs:
                
                solve(row+a , col+b , matrix ,heights[row][col])
        
        if (len(heights) == 0):
            return []
        
        row_size,col_size = len(heights) , len(heights[0])
        
        at = [[0 for _ in range(col_size)] for _ in range(row_size)]
        
        pac = [[0 for _ in range(col_size)] for _ in range(row_size)]
        
        dirs = [(-1,0) , (1,0) , (0,-1) , (0,1)]
        
        # left and right row each for pacific and atlantic
        for row in range(row_size):
            
            solve(row , 0 , at , float('-inf'))
            solve(row, col_size-1 , pac , float('-inf'))
        
        
        # top and bottom column
        for col in range(col_size):
            solve(0 , col , at  ,float('-inf'))
            solve(row_size-1 , col , pac , float('-inf'))
            
        ans = []
        
        for row in range(row_size):
            for col in range(col_size):
                if (at[row][col] and pac[row][col]):
                    ans.append([row,col])
        
        return (ans)

if __name__ == '__main__':

    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    x = 1
    ans = Solution().pacificAtlantic(heights)
    print(ans)