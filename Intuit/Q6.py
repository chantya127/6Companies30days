# Question : Find in Mountain Array

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

# Approach : First find the index of the largest element element in the array using binary search
# then search in two halfs , as left half is sorted in ascending order while the right half is soretd in descending order.
dd = ["", "", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def findInMountainArray(self,arr, target):
        
        def get_peak(low , high):
            
            idx = -1
            while(low <= high):
                
                mid = (high-low)//2 + low
                
                if (arr[mid] < arr[mid+1]):
                    low = mid+1
                
                else:
                    idx = mid
                    high = mid-1
            
            return (idx)
        
        def find_left(low, high):
            
            idx = float('inf')
            
            while(low <= high):
                
                mid = (high-low)//2 + low
                
                val = arr[mid]
                
                if (val >= target):
                    
                    if (val == target):
                        idx = mid
                    high = mid-1
                
                else:
                    low = mid+1
            
            return (idx)
        
        def find_right(low ,high):
            
            idx =float('inf')
            
            while(low <= high):
                
                mid = (high -low)//2 + low
                
                val = arr[mid]
                
                if (val<=target):
                    
                    if (val == target):
                        idx = mid
                    
                    high = mid-1
                
                else:
                    low = mid+1
            
            return (idx)
        
        size = len(arr)
        
        peak = get_peak(0,size-1)
        
        # print(peak)
        left_idx = find_left(0,peak)

        if (left_idx != float('inf')):
            return (left_idx)
        
        right_idx = find_right(peak+1 , size-1)
        
        if (right_idx != float('inf')):
            return (right_idx)
        
        return -1
        

if __name__ == '__main__':

    array = [1,2,3,4,5,3,1]
    target = 3
    obj = Solution()
    ans = obj.findInMountainArray(array,target)
    
    print(ans)