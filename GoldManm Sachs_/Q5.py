# Question : Ugly Numbers .gly numbers are numbers whose only prime factors are 2, 3 or 5. 
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers

# Approach :  Use three pointers p2,p3,p5 and go on adding the val minimum from these 3 pointers when multipliedd by 2,3,5.


# input => n = 10
# output = 12


class Solution:
    def solve(self, n):
        #Code here
        
        # intially 1 number
        dp = [1]
        p2,p3,p5 = 0,0,0

        for i in range(n-1):
		    
            # take minimum value
            mini = min(2*dp[p2] , 3*dp[p3] , 5*dp[p5])
		    
		    # inc p2 ptr if mini caused by p2 ptr
            if (mini == 2*dp[p2]):
                  p2 +=1
		    
            # inc p3 ptr
            if (mini == 3*dp[p3]):
                p3 +=1
		    
            #inc p5 ptr.
            if (mini == 5*dp[p5]):
                p5 +=1
		    
            dp.append(mini)
		
        return (dp[-1])
    
        

if __name__ == '__main__':

    n=10
    obj = Solution()
    ans = obj.solve(n)
    
    print(ans)