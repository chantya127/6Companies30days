# Question :Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.


# Approach : Use binary search to find the maximum possible sum,with low value as max(arr)
# high value as sum of the whole array

class Solution:
    def splitArray(self, nums, m):
        
        def poss(target):
            
            summe = nums[0]
            count = 1
            
            for num in nums[1:]:
                
                summe += num
                if (summe >target):
                    count +=1
                    summe = num
                
                if (count >m):
                    break
            
            return (count <=m)
                    
            
        
        size = len(nums)
        
        prefix = [nums[idx] for idx in range(size)]
        
        for idx in range(1,size):
            prefix[idx] += prefix[idx-1]
        
        
        low = max(nums)
        high =sum(nums)
        
        ans = 0
        
        while(low <= high):
            
            mid = (high -low)//2 + low
            
            if (poss(mid)):
                ans = mid
                high = mid-1
            
            else:
                low = mid+1
        
        return (ans)

if __name__ == '__main__':

    arr = [7,2,5,10,8]; m = 2
    n = len(arr)
    obj = Solution()
    ans = obj.splitArray(arr , m)
    
    print(ans)