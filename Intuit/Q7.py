
# Question :  Capacity To Ship Packages Within D Days

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.


# Approach :  Use binary search to find the minimum nuber of days required to transport the packages.
# low :- max(weights) , high = sum(weights) bcoz if day will be = 1 , then capacity should be sum of all the weights.




class Solution:
    def shipWithinDays(self, weights, days):
        
        def solve(limit):
            
            summe = weights[0]
            count = 1
            
            for idx in range(1,size):
                
                curr = weights[idx]
                if (curr > limit):
                    return False
                
                summe += curr
                if (summe > limit):
                    summe = curr
                    count +=1
                
                if (count > days):
                    break
            
            return (count <= days)
        
        size = len(weights)
        
        low = max(weights)
        
        high = sum(weights)+1
        
        ans =-1
        
        while(low <= high):
            
            mid = (high-low)//2 + low
            # print(mid, low,high)
            if (solve(mid)):
                
                ans = mid
                high = mid-1
            
            else:
                low = mid+1
        
        return (ans)


if __name__ == '__main__':

    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5

    obj = Solution()
    ans = obj.shipWithinDays(weights,days)
    print(ans)