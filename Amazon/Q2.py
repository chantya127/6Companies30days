# Question :Longest Mountain in Array

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.


# Approach :  A pt is called a mountain pt if is greater than both of the numbers on other side.
# so consider each mountain pt and calculate its size




class Solution:
    def longestMountain(self, arr):
        
        size = len(arr)
        
        if (size <3):
            return 0
        
        idx = 1
        
        ans = 0
        while(idx <size-1):
            
            if (arr[idx] > arr[idx-1] and arr[idx]>arr[idx+1]):
                
                count = 1
                
                left = idx
                while(left>0 and arr[left] > arr[left-1]):
                    
                    left-=1
                    count +=1
                
                while(idx<size-1 and arr[idx] > arr[idx+1]):
                    idx +=1
                    count +=1
                
                ans = max(ans ,count)
            
            else:
                idx +=1
        
        return (ans)

if __name__ == '__main__':

    
    arr = [2,1,4,7,3,2,5]
    obj = Solution()
    ans = obj.longestMountain(arr)

    print(ans)

    # done