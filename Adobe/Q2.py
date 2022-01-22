# Question :Given an array called A[] of sorted integers having no duplicates, find the length of the Longest Arithmetic Progression (LLAP) in it.


# Input: N = 6
# set[] = {1, 7, 10, 13, 14, 19}
# Output: 4
# Explanation: The longest arithmetic 
# progression is {1, 7, 13, 19}.

# Approach :  Use dynamic programming apporach .
# for each index store the diff with freq of how many times diff is occurring at a particular index.


class Solution:
    def lengthOfLongestAP(self, arr, size):
        # code here
        if (size ==0):
            return 0
            
        dp = [{} for i in range(size)]
        
        ans = 1
        
        for idx in range(1,size):
            
            for ptr in range(idx):
                
                diff = arr[idx] - arr[ptr]
                if (diff in dp[ptr]):
                    
                    dp[idx][diff] = dp[ptr][diff]+1

                else:
                    dp[idx][diff] = 2

                ans = max(ans ,dp[idx][diff])
        
        return (ans)

if __name__ == '__main__':

    
    arr = [1, 7, 10, 13, 14, 19]
    n = len(arr)
    obj = Solution()
    ans = obj.lengthOfLongestAP(arr,n)

    print(ans)

    # done