

# Link: https://practice.geeksforgeeks.org/problems/overlapping-rectangles1924/1/

# Question : Greatest Common Divisor of Strings

# Approach :  Apply eucledian algorithm of calculating gcd of two numbers on two strings.            



# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"


class Solution:
    def solve(self, str1,str2):
    
        def find_gcd(a,b):
            
            if (b == 0):
                return a
        
            return (find_gcd(b , a%b))
        
        # if two strings oderings is different,it is not  possible to find gcd
        if (str1 +str2) != (str2 + str1):
            return ""
        
        n,m = len(str1), len(str2)
        gcd = find_gcd(n,m)
        
        # finally return smaller string till gcd
        return (str2[:gcd])

if __name__ == '__main__':

    str1 = "ABCABC"
    str2 = "ABC"
    obj = Solution()
    ans = obj.solve(str1,str2)
    print(ans)