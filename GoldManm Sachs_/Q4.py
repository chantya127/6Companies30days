# Question : Run Length Encoding

# Approach :  Just calculate the count of the characters on the fly and add it to current answer.



# str = aaaabbbccc
#Output: a4b3c3
# output = 7  a repeated 4 times consecutively b 3 times, c also 3 times.




class Solution:
    def solve(self, arr):
        #Code here
    
        ans = ""
        ptr = 0
        size= len(arr)
        
        while(ptr <size):
            
            curr = arr[ptr]
            count = 0
            while(ptr <size and arr[ptr] == curr):
                count +=1
                ptr +=1
            
            ans += curr + str(count)
        
        return (ans)

if __name__ == '__main__':

    arr = "abbbcdddd"
    size = len(arr)
    obj = Solution()
    ans = obj.solve(arr)
    print(ans)