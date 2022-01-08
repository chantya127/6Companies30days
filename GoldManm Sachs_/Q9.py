
# Question : Given a pattern containing only I's and D's. I for increasing and D for decreasing.
# Devise an algorithm to print the minimum number following that pattern.
# Digits from 1-9 and digits can't repeat.


# Input : str = iidd

# Output : 12543

# Approach : Use stack .Keep adding the curr_val in stack if val is "d" . 
# Else pop all the elements when the operation is I.

class Solution:
    def solve(ob,S):
        # code here 
        
        stack = []
        
        curr_num = 1
        
        ans = ""
        
        for pat in S:
            
            stack.append(curr_num)
            curr_num +=1
            if (pat == "I"):
                
                while(stack):
                    num = stack.pop()
                    ans+= str(num)
        
        stack.append(curr_num)
        while(stack):
            num = stack.pop()
            ans += str(num)
            
        return (ans)
if __name__ == '__main__':

    S = "iidd"
    obj = Solution()
    ans = obj.solve(S)
    print(ans)