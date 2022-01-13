# Question : Maximum of subarrays of size k


# Input:
# N = 9, K = 3
# arr[] = 1 2 3 1 4 5 2 3 6
# Output: 
# 3 3 4 5 5 5 6 
# Explanation: 
# 1st contiguous subarray = {1 2 3} Max = 3
# 2nd contiguous subarray = {2 3 1} Max = 3
# 3rd contiguous subarray = {3 1 4} Max = 4
# 4th contiguous subarray = {1 4 5} Max = 5
# 5th contiguous subarray = {4 5 2} Max = 5
# 6th contiguous subarray = {5 2 3} Max = 5
# 7th contiguous subarray = {2 3 6} Max = 6


# Approach :  Use sliding window approach with the help of deque.
# Pop smaller elements than curr element or out  of window from current element

from collections import deque

class Solution:
    def max_of_subarrays(self,arr,n,k):
        #code here
        
        ququ = deque()
        
        for i in range(k):
            
            curr = arr[i]
            while(ququ and ququ[-1][1] <= curr):
                ququ.pop()
            
            ququ.append((i,curr))
        ans = []
        for i in range(k,n,1):
            
            first = ququ[0][1]
            ans.append(first)
            curr = arr[i]
            while(ququ and i- ququ[0][0] >=k):
                ququ.popleft()
            
            while(ququ and ququ[-1][1] <= curr):
                ququ.pop()
            
            ququ.append((i,curr))
        
        first = ququ[0][1]
        ans.append(first)
        return ans

if __name__ == '__main__':

    k = 3
    arr = [1,2,3,1,4,5,2,3,6]
    size = len(arr)
    obj = Solution()
    ans = obj.max_of_subarrays(arr,size,k)
    print(ans)