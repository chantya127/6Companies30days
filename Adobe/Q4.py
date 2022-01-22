# Question :Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.


# Input: N = 4
# arr = {1, 5, 11, 5}
# Output: YES
# Explaination: 
# The two parts are {1, 5, 5} and {11}.


# Approach : Add one by one sum in dp and check if target is there in dp.



class Solution:
    def equalPartition(self, N, arr):
        # code here
        s = sum(arr)
        if s&1: return 0
        s = s//2
        dp = {0}
        for i in arr: 
            dp.update({x+i for x in dp})
            if s in dp: return 1
        return 0
        


if __name__ == '__main__':

    arr = [1,5,5,11]
    ans = Solution().equalPartition(len(arr),arr)
    print(ans)