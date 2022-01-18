
# Question :Given a number N. The task is to generate and print all binary numbers with decimal values from 1 to N.

# Input:
# N = 2
# Output: 
# 1 10
# Explanation: 
# Binary numbers from
# 1 to 2 are 1 and 10.

# Approach : Iterate through 1-n and add all the binary number to ans

from operator import ge


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def generate(N):
    # code here
    
    def find_bin(num):
        
        res = ""
        
        while(num):
            
            rem = num&1
            
            num = num//2
            
            res += str(rem)
        
        return (res[::-1])
            
    
    ans = []
    for num in range(1,n+1):
        
        val = find_bin(num)
        ans.append(val)
    
    return (ans)

if __name__ == '__main__':

    n = 10
    ans = generate(n)
    print(ans)