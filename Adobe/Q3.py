# Question : Find the number of unique words consisting of lowercase alphabets only of length N that can be formed with at-most K contiguous vowels. 


# Input:
# N = 1
# K = 0
# Output:
# 21
# Explanation:
# All 21 consonants.


# Approach : At any moment we can add consonant ,but for adding a vowel check if continous vowels is less
# than k.

mod = 10**9+7

class Solution:
    def kvowelwords(self, n,k):
        # code here
        
        def solve(pos , vowels):
            
            if (pos == n):
                return 1
               
            # case 1 : 12 consonants
          #  if (vowels == k):
          #      rem = n-pos
          #      return (21**rem)%mod
          
            if (dp[pos][vowels] != -1):
                return (dp[pos][vowels])
                
            v1 = solve(pos+1 , 0)*(21)
            v2 = 0
            
            #  case 2 : vowels
            if (vowels < k):
                v2 = solve(pos+1 , vowels+1)*(5)
            
            dp[pos][vowels]= (v1 + v2)%mod
            return (dp[pos][vowels])
        
        ans = 0
        dp = [[-1 for _ in range(k+1)] for _ in range(n)]
        ans = solve(0,0)
        return ans

if __name__ == '__main__':

    
    k = 0
    n = 1
    obj = Solution()
    ans = obj.kvowelwords(n,k)

    print(ans)