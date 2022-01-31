
# Question :Maximum Performance of a Team

# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# Output: 60
# Explanation: 
# We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

# Approach : Use greedy approach and sort the  combined array in desc order in terms of effiecieny. 
# at any moment ,the current engineer will have min eff and if length of heap == k , then remove the engineer with minimum speed


from heapq import heappush as push, heappop as pop
mod = 10**9+7

class Solution:
    def maxPerformance(self, n: int, speed, eff, k: int) -> int:
        
        poss = [[speed[idx] ,eff[idx]] for idx in range(n)]
        poss.sort(key = lambda it :it[1] , reverse = True)
        
        ans = 0
        heap = []
        summe = 0
        
        for idx in range(n):
            
            sp , e = poss[idx][0],poss[idx][1]
            
            if (len(heap) == k):
                summe -= pop(heap)
            
            summe += sp
            push(heap , sp)
            curr_per = e * summe
            ans = max(ans , curr_per)
            
            
        return (ans)%mod

if __name__ == '__main__':

    n = 6
    speed = [2,10,3,1,5,8]
    efficiency = [5,4,3,9,7,2]
    k = 2
    obj = Solution()
    ans = obj.maxPerformance(n,speed,efficiency,k)
    print(ans)