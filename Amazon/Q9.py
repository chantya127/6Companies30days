
# Question : iven an incomplete Sudoku configuration in terms of a 9x9  2-D square matrix(mat[][]) the task to check if the current configuration is valid or not
# where a 0 represents an empty block.


# Input: mat[][] = [
# [3, 0, 6, 5, 0, 8, 4, 0, 0]
# [5, 2, 0, 0, 0, 0, 0, 0, 0]
# [0, 8, 7, 0, 0, 0, 0, 3, 1]
# [0, 0, 3, 0, 1, 0, 0, 8, 0]
# [9, 0, 0, 8, 6, 3, 0, 0, 5]
# [0, 5, 0, 0, 9, 0, 6, 0, 0]
# [1, 3, 0, 0, 0, 0, 2, 5, 0]
# [0, 0, 0, 0, 0, 0, 0, 7, 4]
# [0, 0, 5, 2, 0, 6, 3, 0, 0]
# ]

# Output: 1
# Explaination: It is possible to have a
# proper sudoku.

# Approach : Use dictionary to mark the values and their corresponding location.
# now check if the value values in same row or col or same 3*3 sub-square

class Solution:
    def isValid(self, matrix):
        # code here
        
        def check(x1,y1 , x2,y2):
            
            if (x1//3 == x2//3 and y1//3 == y2//3):
                return True
            
            else:
                return (False)
        
        row,col = len(matrix) , len(matrix[0])
        
        mark = {}
        
        for idx in range(row):
            for ptr in range(col):
                
                curr = matrix[idx][ptr]
                if (curr != 0):
                    
                    if (curr not in mark):
                        mark[curr] = [(idx,ptr)]
                    
                    else:
                        for (x,y) in mark[curr]:
                            
                            if (x == idx) or (ptr == y) or check(idx,ptr,x,y):
                                return 0
                        
                        mark[curr] += [(idx,ptr)]
                        
        
        return (1)

if __name__ == '__main__':

    mat = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    obj = Solution()
    ans = obj.isValid(mat)
    print(ans)