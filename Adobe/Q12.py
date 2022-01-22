
# Question : Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.


# Input:
# N = 5, K = 3
# A[] = {0,0,2,1,1}
# Output: 0 0 1 2 $
# Explanation: Sum of 0, 0, 1, 2 is equal to K.

# apporach : Use two ptr approach but with the help of 4 ptrs.
# increment the ptrs when the curr and prev elements are the same.

class Solution:
    def fourSum(self, arr, target):
        # code here
        
        arr.sort()
        size = len(arr)
        count = []
        for p1 in range(size-3):
            
            if (p1 >0 and arr[p1] == arr[p1-1]):
                continue
            
            for p2 in range(p1+1,size-2,1):
                
                if (p2 > p1+1 and arr[p2] == arr[p2-1]):
                    continue
                
                p3 = p2+1
                p4 = size-1
                summe = 0
                while(p3 < p4):
                    
                    summe = arr[p3] + arr[p4] +arr[p1] + arr[p2]
                    if (summe == target):
                        
                        if (p3 > p2+1 and p4<size-1 and arr[p3] == arr[p3-1] and arr[p4] == arr[p4+1]):
                            p3 +=1
                            p4 -=1
                        
                        else:
                            count.append([arr[p1] ,arr[p2] , arr[p3] ,arr[p4]])
                            p3 +=1
                            p4 -=1
                    
                    elif (summe > target):
                        p4 -=1
                    
                    else:
                        p3 +=1
        
        return (count)

if __name__ == '__main__':

    n = 5
    arr = [0,0,2,1,1]
    k= 3
    obj = Solution()
    ans = obj.fourSum(arr ,k)
    print(ans)