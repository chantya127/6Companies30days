# Question :Given a matrix of size r*c. Traverse the matrix in spiral form.


# Input:
# r = 4, c = 4
# matrix[][] = {{1, 2, 3, 4},
#            {5, 6, 7, 8},
#            {9, 10, 11, 12},
#            {13, 14, 15,16}}
# Output: 
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10


# Approach :Maintain four boundary ptrs left ,right,up,down and 
# accordingly traverse the matrix.


def spirallyTraverse(matrix, r, c): 
    # code here 
    ans = []
    move = 0
    left =0
    right = c-1
    up = 0
    down = r-1
    while (left<=right) and (up<=down):
        
        # from left to right
        if move == 0:
            for i in range(left , right+1):
               ans.append(matrix[up][i])
              
            up+=1

        # from up to down
        if move == 1:
            for i in range(up ,down+1):
                ans.append(matrix[i][right])
            right-=1


        # from right to left
        if move == 2:
            for i in range(right , left-1,-1):
                ans.append(matrix[down][i])
            down-=1


        # from bottom to up
        if move == 3:
            for i in range(down , up-1 , -1):

                ans.append(matrix[i][left])
            left+=1
        move = (move+1)%4
        
        
    return ans
        


if __name__ == '__main__':

    r = 4;c = 4
    matrix = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15,16]]
    ans = spirallyTraverse(matrix,r,c)
    print(ans)