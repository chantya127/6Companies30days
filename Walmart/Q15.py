
# Question :Divide Two Integers


# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.


# Approach : use bitmasking and increase the divisor in powers to reduce the time complexity.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        sign = 1
        
        
        if (dividend<0)^(divisor<0):
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quo = 0
        while(dividend >= divisor):
            
            temp = divisor
            power = 1
            while(temp <<1 <= dividend):
                
                temp = temp<<1
                power = power <<1
            
            dividend -= temp
            quo += (power)
        
        return quo*sign  

if __name__ == '__main__':

    dividend = 10; divisor = 3
    obj = Solution()
    ans = obj.divide(dividend,divisor)
    print(ans)