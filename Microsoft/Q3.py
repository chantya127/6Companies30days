# Question : Given a square matrix[][] of size N x N. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.


# Input:
# N = 3
# matrix[][] = [[1 2 3],
#               [4 5 6],
#               [7 8 9]]
# Output:
# 3 6 9 
# 2 5 8 
# 1 4 7


# Approach : Just find the transpose of the matrix.
# Then swap first row with last row ,2nd row with 2nd last row and so on.


def rotate(matrix): 
    #code here
    
    row_size ,col_size = len(matrix) , len(matrix[0])
    
    for row in range(row_size):
        for col in range(row+1,col_size):
            
            if(row != col):
                matrix[row][col] , matrix[col][row] = matrix[col][row] ,matrix[row][col]
    
    st = 0
    end = row_size-1

        
    while(st < end):
        
        for col in range(col_size):
            
            matrix[st][col] , matrix[end][col] = matrix[end][col] , matrix[st][col]
        
        st +=1
        end -=1

if __name__ == '__main__':

    matrix = [ [1 ,2, 3],[4, 5, 6],[7,8, 9]]
        
    for row in matrix:
        print(row)
    
    print()

    rotate(matrix)
    for row in matrix:
        print(row)