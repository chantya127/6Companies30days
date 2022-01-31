
# Question : Maximum Height Tree

# Input: n = 10
# Output: 4
# Explaination: With 10 dots we can complete 
# total four lines. The layers will have 1, 
# 2, 3 and 4 dots respectively.
 

# Approach :  Go on adding the levels one by one till the total sum is <= n.


class Solution:
    def height(self, n):
        # code here
        
        if (n == 1):
            return n
        
        level = 0
        curr_sum = 0
        while(curr_sum <= n):
            
            curr_sum += level+1
            
            level +=1
            
        return level-1

if __name__ == '__main__':

    n = 10
    obj = Solution()
    ans = obj.height(n)
    print(ans)