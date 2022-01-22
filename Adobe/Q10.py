
# Question : Stickler Thief


#Input:
# n = 6
# a[] = {5,5,10,100,10,5}
# Output: 110
# Explanation: 5+100+5=110

# Approach : Use Inc exc principle to find the maximum profit

class Solution:
    def FindMaxSum(self,arr, n):
        
        size= len(arr)
        if (size <3):
            return max(arr)
        
        inc,exc = arr[0] , 0
        
        for idx in range(1,size):
            
            cinc = arr[idx] + exc
            cexc = max(inc,exc)
            
            inc = cinc
            exc = cexc
            
        
        return max(inc,exc)

if __name__ == '__main__':

    arr = [5,5,10,100,10,5]
    obj = Solution()
    ans = obj.FindMaxSum(arr , len(arr))
    print(ans)