
# Question : Given an infinite number line. 
# You start at 0 and can go either to the left or to the right. The condition is that in the ith move, youmust take i steps. 
# Given a destination D , find the minimum number of steps required to reach that destination.


# Input: D = 2
# Output: 3
# Explaination: The steps takn are +1, -2 and +3.


# Approach :  go on adding step to summe ,when summe equals to target return step
# otherwise check if (summe - target)%2 ==0 , meaning any two numbers can be reduced.


class Solution:
    def minSteps(self, target):
        # code here
        target = abs(target)
        
        summe ,step = 0,0
        while(True):
            
            step +=1
            summe +=step
            
            if (summe == target):
                return (step)
            
            if (summe >target and (summe - target)%2 ==0):
                return (step)

if __name__ == '__main__':

    d = 2
    obj = Solution()
    ans = obj.minSteps(d)
    print(ans)
