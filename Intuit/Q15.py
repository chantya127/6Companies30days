
# Question : Koko Eating Bananas

# Input: Input: piles = [3,6,7,11], h = 8
# Output: 4

# Approach : Apply binary search , for each possible speed .
# calculate for each pile of banana , and check if it is possible to finish all within the time limit.


from math import ceil

class Solution:
    def minEatingSpeed(self, piles, h):
        
        def pos(speed):
            
            time = 0
            
            for ban in piles:
                
                time+= ceil(ban/speed)
            
            return (time <= h)
        
        low = 1
        high = max(piles)
        ans = -1
        
        
        while(low <= high):
            
            mid = (high-low)//2 + low
            
            if (pos(mid)):
                ans = mid
                high = mid-1
            
            else:
                low = mid+1
        
        return (ans)    

if __name__ == '__main__':

    piles = [3,6,7,11]
    h = 8
    ans = Solution().minEatingSpeed(piles,h)
    print(ans)