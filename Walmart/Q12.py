
# Question : Find Array Given Subset Sums

# Input: n = 3, sums = [-3,-2,-1,0,0,1,2,3]
# Output: [1,2,-3]
# Explanation: [1,2,-3] is able to achieve the given subset sums:
# - []: sum is 0
# - [1]: sum is 1
# - [2]: sum is 2
# - [1,2]: sum is 3
# - [-3]: sum is -3
# - [1,-3]: sum is -2
# - [2,-3]: sum is -1
# - [1,2,-3]: sum is 0
# Note that any permutation of [1,2,-3] and also any permutation of [-1,-2,3] will also be accepted.

from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums):
        
        sums.sort()
        ans = []
        
        while(len(sums) >1):
            
            num = sums[-1] - sums[-2]
            count = Counter(sums)
            
            inc , exc= [],[]
            
            for x in sums:
                
                if(count[x] > 0):
                    
                    exc.append(x)
                    inc.append(num+x)
                    count[x] -=1
                    count[x+num] -=1
            
            if (0 in exc):
                sums = exc
                ans.append(num)
            
            else:
                sums = inc
                ans.append(-1*(num))
        
        return (ans)

if __name__ == '__main__':
    obj = Solution()

    n = 3; sums = [-3,-2,-1,0,0,1,2,3]

    ans = obj.recoverArray(n,sums)

    print(ans)