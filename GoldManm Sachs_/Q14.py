
# Question : Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.


# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


# Approach :  Use two pointer approach.Keep adding the elements to the current window till the summe is less than k.
# when sume >= k ,then start reducing the size of the curr_window.



class Solution:
    def solve(self, target ,nums):
    
        sec = 0
        size = len(nums)
        ans = float('inf')
        summe= 0
        
        for first in range(size):
            
            summe += nums[first]
            
            while(summe >= target):
                
                curr_len = first - sec+1
                ans = min(ans , curr_len)
                summe -= nums[sec]
                sec +=1
        
        return ans if ans !=float('inf') else 0

if __name__ == '__main__':

    target = 7
    nums = [2,3,1,2,4,3]
    obj = Solution()
    ans = obj.solve(target ,nums)
    print(ans)