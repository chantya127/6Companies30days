
# Question : Decode the string.An encoded string (s) is given, the task is to decode it.



# Input: s = 3[b2[ca]]
# Output: bcacabcacabcaca


# Approach :Use two stacks one for num and chars. Then whenever opening braces is seen add the current string on the  stack
# and start a new current string.
# If closing braces is seen , then pop the cache string and number from num_stack.


class Solution:
    def solve(self, s):
        # code here
        
        num_stack = []
        string_stack = []
        
        curr_string = ""
        ptr = 0
        size= len(s)
        
        while(ptr < size):
            
            curr_char = s[ptr]
            if (curr_char == '['):
                string_stack.append(curr_string)
                curr_string = ""
                ptr +=1
            
            elif (curr_char == ']'):
                
                num = num_stack.pop()
                prev_string = string_stack.pop()
                
                curr_string = prev_string + curr_string*num
                
                ptr +=1
            
            elif(curr_char.isdigit()):
                
                num = 0
                while(ptr <size and s[ptr].isdigit()):
                    
                    num = num*10 + int(s[ptr])
                
                    ptr +=1
                
                num_stack.append(num)
            
            else:
                curr_string += curr_char
                ptr +=1
        
        return (curr_string.strip())

if __name__ == '__main__':

    s = "3[b2[ca]]"
    obj = Solution()
    ans = obj.solve(s)
    print(ans)