# Question :Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.


# Input: N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.


# Approach :Use two pointer apporach . Go on adding the numbers till the sum is less than target
# check if summe becomes equal to the target


class Solution:
    def subArraySum(self,arr, n, s):
        
        start,end = 0,0
        summe = 0
        flag = 0
        
        while(end < n+1):
            
            if (summe > s):
                
                summe -= arr[start]
                start+=1
            
            elif (summe == s):
                flag = 1
                break
        
            else:
                if (end <n):
                    summe += arr[end]
                
                end +=1
        
        if (flag):
            return [start+1,end]
        
        return [-1]

if __name__ == '__main__':

    
    
    arr = [1,2,3,7,5]
    n = len(arr)

    summe = 12

    obj = Solution()
    ans = obj.subArraySum(arr,n,summe)
    print(ans)