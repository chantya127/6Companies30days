

# Link: https://practice.geeksforgeeks.org/problems/overlapping-rectangles1924/1/

# Question : Count the subarrays having product less than k 

# Approach :  Use 2 pointer technique. Go on multiplying the numbers till the given product
#             is less than k.If the product becomes greater than k , then use sec pointer and 
#              start reducing the current window size.            



# input => n = 4, k = 10
# a[] = {1, 2, 3, 4}
# output = 7  (The contiguous subarrays are {1}, {2}, {3}, {4} {1, 2}, {1, 2, 3} and {2, 3} whose count is 7.)




class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
    
        end = 0
        prod = 1
        count = 0
        
        for start in range(n):
            
            curr = a[start]
            prod *= curr
            while(prod >=k):
                
                prev = a[end]
                end +=1
                prod //=prev
            
            count += start-end+1
        
        return (count)

if __name__ == '__main__':

    k = 10
    arr = [1,2,3,4]
    size = len(arr)
    obj = Solution()
    ans = obj.countSubArrayProductLessThanK(arr,size,k)
    print(ans)