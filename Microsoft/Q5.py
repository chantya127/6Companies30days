# Question :The stock span problem is a financial problem where we have a series of n daily price quotes for a stock
#  and we need to calculate the span of stock’s price for all n days. 

# Input: 
# N = 7, price[] = [100 80 60 70 60 75 85]
# Output:
# 1 1 1 2 1 4 6
# Explanation:
# Traversing the given input span for 100 
# will be 1, 80 is smaller than 100 so the 
# span is 1, 60 is smaller than 80 so the 
# span is 1, 70 is greater than 60 so the 
# span is 2 and so on. Hence the output will 
# be 1 1 1 2 1 4 6.

# Approach : Use stack and apply next greater element on the right logic.
# Pop from the stack if current element is greater or equal to the top of the stack.


dd = ["", "", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]

class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        
        stack = []
        ans = [0]*(n)
        # ans[0] = 1
        
        for i in range(n):
            
            curr = a[i]
            last = i
            while(stack and a[stack[-1]]<= curr):
                stack.pop()
            
            if (stack):
                ans[i] = i -stack[-1]
            
            else:
                ans[i] = i+1
            stack.append(i)
        
        return (ans)
        

if __name__ == '__main__':

    arr = [100, 80,60 ,70 ,60 ,75, 85]
    n = len(arr)
    obj = Solution()
    ans = obj.calculateSpan(arr,n)
    
    print(ans)