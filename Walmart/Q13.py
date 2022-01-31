
# Question :  Find the Kth Largest Integer in the Array

# Input: nums = ["3","6","7","10"], k = 4
# Output: "3"
# Explanation:
# The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
# The 4th largest integer in nums is "3".

# approach : Apply min heap approach and pop from the heap , is size of the heap is greater than k

from heapq import heappush as push , heappop as pop


class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        
        nums = [int(num) for num in nums]
        
        heap = []
        size = len(nums)
        for idx in range(size):
            
            curr = nums[idx]
            push(heap,curr)
            if (len(heap) > k):
                pop(heap)

        return str(heap[0])

if __name__ == '__main__':
    obj = Solution()

    nums = ["3","6","7","10"]; k = 4

    ans = obj.kthLargestNumber(nums,k)

    print(ans)