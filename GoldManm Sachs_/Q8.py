
# Question : Total Decoding Messages 
# A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# You have to decode it


# Input : str= 123
#Output : 3 . It can be decoded as as (ABC , AW, LC)


# Approach : Use Dp Approach. Check is prev char is non-zero . Then add prev value .
# The string size can be of two letters as well check if prev two charcters are between 10 - 26



mod = 10**9+7

class Solution:
    def solve(self, string):
		# Code here
		
        if(string[0] == "0"):
            return 0
        
        size = len(string)
        dp = [0]*(size+1)
	
        dp[0] = 1
        dp[1] = 1
		
        for idx in range(2,size+1):
		    
            if (string[idx-1] >'0'):
                dp[idx] = dp[idx-1]
		    
            # check prev two characters greater >10 and  less than < 27
            if (string[idx-2] == '1' or (string[idx-2] == '2') and string[idx-1] < '7'):   
                dp[idx] = (dp[idx] + dp[idx-2])%mod
		
        return (dp[-1])

if __name__ == '__main__':

    str= "123"
    obj = Solution()
    ans = obj.solve(str)
    print(ans)