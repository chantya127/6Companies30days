# Question :Given a 2D board of letters and a word. Check if the word exists in 
# the board. The word can be constructed from letters of adjacent cells only. ie - horizontal or vertical neighbors. The same letter cell can not be used more than once.


# Example 1:

# Input: board = {{a,g,b,c},{q,e,e,l},{g,b,k,s}},
# word = "geeks"
# Output: 1
# Explanation: The board is-
# a g b c
# q e e l
# g b k s
# The letters which are used to make the
# "geeks" are colored.

# Approach :  Just use dfs from the starting letter in all directions and see if it is possible
# to form the target word or node
from collections import defaultdict


class Solution:
    def isWordExist(self, board, word):
        #Code here
        
        def solve(row,col , idx):
            
            if(idx == size):
                return True
            
            if (row<0 or col <0 or row>=row_size or col >= col_size or vis[row][col] == 1):
                return False
            
            vis[row][col] = 1
            
            for (a,b) in dirs:
                
                nrow,ncol = row+a ,col+b
                
                if(0 <= nrow<row_size and 0 <= ncol <col_size and vis[nrow][ncol] == 0):
                    
                    if (board[nrow][ncol] == word[idx]):
                        
                        val = solve(nrow,ncol , idx+1)
                        if (val):
                            return (True)
                            
            vis[row][col] = 0
            return (False)
                        
        
        dirs = [(-1,0) , (1,0) , (0,-1) , (0,1)]
        
        size = len(word)
        row_size , col_size = len(board) , len(board[0])
        
        vis=[[0 for _ in range(col_size)] for _ in range(row_size)]
        
        for row in range(row_size):
            
            for col in range(col_size):
                
                curr = board[row][col]
                
                if (curr == word[0]):
                    
                    val = solve(row,col , 1)
                    if (val):
                        return (True)
        
        return (False)

if __name__ == '__main__':

    
    board = [['agbc'],['qeel'],['gbks']]
    word = "geeks"
    prerequisites = [[1,0],[2,1],[3,2]]
    obj = Solution()
    ans = obj.isWordExist(board,word)

    print(ans)

    # done