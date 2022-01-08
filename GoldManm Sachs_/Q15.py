
# Question : Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.


# Input : arr = [9, 5, 7, 3], k = 6
# Output: True
# Explanation: {(9, 3), (5, 7)} is a possible solution. 9 + 3 = 12 is divisible
# by 6 and 7 + 5 = 12 is also divisible by 6.

# Approach : Use Hashmaps to store the count of rem of each num.
# If number is multiple of k or number is divsible by k .Then frequency of that number should be even.
# If suppose freq of x rem is c1 . Then freq of (k-x) should also be c1.



from collections import defaultdict
class Solution:

    def solve(self, nums, k):
                
        mapping = defaultdict(int)
        for num in nums:
            rem = num%k
            mapping[rem] += 1
        
        for num in nums:
            
            key = num%k
            
            if (key == 0):
                if (mapping[key]%2 ==1):
                    return False
            
            elif (key*2 == k):
                
                if (mapping[key]%2 == 1):
                    return False
                    
            else:
                f1 = mapping[key]
                f2 = mapping[k - key]
                
                if (f1 != f2):
                    return False
                
        return True

if __name__ == '__main__':

    arr = [9, 5, 7, 3]
    k = 6
    obj = Solution()
    ans = obj.solve(arr,k)
    print(ans)