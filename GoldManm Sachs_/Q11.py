
# Question : Find Missing And Repeating  number from array.

# Input : arr = [2,3,3,4]

# Output : 1 and 3

# Approach : Calculate the non_rep sum and sum of the entir array.
# missing element -> total_sum_upto_n - non_rep_sum
# repeating_element -> sum(arr) - non_rep_sum


class Solution:
    def solve(self, arr):
    
        size = len(arr)
        non_rep = set(arr)

        non_rep_sum = sum(non_rep)

        total_sum_upto_n = ((size)*(size+1))//2

        missing_num = total_sum_upto_n - non_rep_sum

        rep_num = sum(arr) - non_rep_sum

        return [missing_num , rep_num]

if __name__ == '__main__':

    arr = [2,3,3,4]
    obj = Solution()
    ans = obj.solve(arr)
    print(ans)