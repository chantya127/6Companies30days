
# Question : stributing M items in a circle of size N starting from K-th position

# Approach :  Reduce to zero index by subtracting by 1 and then add K and finally take mode by N to get the position.



# Input : N = 5 // Size of circle
#         M = 2 // Number of items
#         K = 1 // Starting position

# Output : 2
# The first item will be given to 1st 
# position. Second (or last) item will 
# be delivered to 2nd position


class Solution:
    def solve(self, n,m,k):
    
        val= (m+k-1)%n

        if (val == 0):
            return (n)
        
        else:
            return (val)

if __name__ == '__main__':

    n,m,k = 5,2,1
    obj = Solution()
    ans = obj.solve(n,m,k)
    print(ans)