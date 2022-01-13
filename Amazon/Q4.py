# Question : Brackets in Matrix Chain Multiplication

# Input: 
# n = 5
# p[] = {1, 2, 3, 4, 5}
# Output: (((AB)C)D)
# Explaination: The total number of 
# multiplications are (1*2*3) + (1*3*4) 
# + (1*4*5) = 6 + 12 + 20 = 38.


# Approach : Use dp approach with 2 pointer technique



class Solution:
    def matrixChainOrder(self, arr, n):
        # code here

        def print_parenthis( i , j , n ,ptr):
    
            if i==j:
                print(chr(ptr[0]),end='')
                ptr[0]+=1
                return
            print("(",end='')
            print_parenthis(i , bracket[i][j] , n , ptr)
            print_parenthis(bracket[i][j]+1 , j , n ,ptr)
            print(")",end='')
    

        def solve(arr , i , j ,t):
            if i>=j:
                return 0
            
            if t[i][j]!=-1:
                return t[i][j]
            
            mini = 9999999999999
            for k in range(i , j):
                temp = solve(arr , i ,k,t) +solve(arr , k+1 , j ,t) + (arr[i-1] *arr[k]*arr[j])
                if temp < mini:
                    mini = temp
                    bracket[i][j] = k
            t[i][j] =  mini    
            return mini
        
        i = 1
        j = n-1
        t = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        bracket = [[-1  for _ in range(n+1)] for _ in range(n+1)]
        solve(arr ,i ,j ,t)
        print_parenthis(1 , n-1 , n  ,[65])
        # print('fff')
        


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]
    size = len(arr)
    obj = Solution()
    obj.matrixChainOrder(arr,len(arr))
    #print(ans)