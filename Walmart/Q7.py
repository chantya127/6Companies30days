# Question :Given an array A of N integers, find any 3 elements in it such that A[i] < A[j] < A[k] and i < j < k.


# Input:
# N = 5
# A[] = {1,2,1,1,3}
# Output: 1
# Explanation: a sub-sequence 1 2 3 exist.


# Approach : Take two arr . left small and right_big.
# now for each index ,calculate left_small and right_big.


class Solution:
    def find3number(self,arr, size):
        # code here
        
        
        left_small = [-1]*(size)
        right_big = [-1]*(size)
        
        prev = arr[0]
        
        for idx in range(1,size-1,1):
            
            curr = arr[idx]
            if (curr > prev):
                left_small[idx] = prev
            
            prev = min(prev ,curr)
        
        prev = arr[-1]
        for idx in range(size-2,0,-1):
            curr = arr[idx]
            if (curr < prev):
                right_big[idx] = prev
            
            prev = max(prev  ,curr)
        
        for idx in range(1,size-1,1):
            if (left_small[idx] != -1 and right_big[idx] != -1):
                return [left_small[idx] , arr[idx] , right_big[idx]]
        
        return []
        

if __name__ == '__main__':

    arr = [1,2,1,1,3]
    n = len(arr)
    obj = Solution()
    ans = obj.find3number(arr,n)
    
    print(ans)