# Question :Largest number in K swaps

# Input: K = 4
# str = "1234567"
# Output:
# 7654321
# Explanation:
# Three swaps can make the
# input 1234567 to 7654321, swapping 1
# with 7, 2 with 6 and finally 3 with 5


# Approach : Try each and every possible combination and return the maximum one from it.

class Solution:
    
    def swap(self , s , i , j):
        
        ith = s[i]
        jth = s[j]
        left = s[:i]
        right = s[j+1:]
        midd = s[i+1:j]
        return left + jth + midd + ith +right
    
    def solve(self , s , k , maxi):
        
        if k==0:
            return
        
        for i in range(len(s) -1):
            for j in range(i+1 , len(s) , 1):
                if s[j] > s[i]:
                    s = self.swap(s , i ,j)
                    if s > maxi[0]:
                        maxi[0] = s
                    self.solve(s , k -1 , maxi)
                    s = self.swap(s , i ,j)
                    
        
    
    def findMaximumNum(self,s,k):
        
               
        maxi = [s]
        self.solve(s , k , maxi)
        return str(maxi[0])
        


if __name__ == '__main__':

    obj = Solution()
    K = 4
    string = "1234567"
    ans = obj.findMaximumNum(string,K)
    print(ans)