
# Question : Squares in N*N Chessboard 


# Input : n=5

# Output : 55

# Approach : Actually the sum of any n is sum of all the squares upto n.
# squared in n*n chessboard => 1^2 + 2^2 + 3^2 + 4^2 + 5^2 +...+n^n
# the formuala ((n)*(n+1)*(2*n+1))//6



class Solution:
    def solve(self, n):
    
        return ((n)*(n+1)*(2*n+1))//6

if __name__ == '__main__':

    n = 5
    obj = Solution()
    ans = obj.solve(n)
    print(ans)