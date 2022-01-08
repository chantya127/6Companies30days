# Question :Given two rectangles, find if the given two rectangles overlap or not

# input => L1=(0,10) , R1=(10,0) , L2=(5,5) ,R2=(15,0)
# output = 1 (Overlapping)


# Approach :  Just check if one rectangle is on the left or top side
              # of the other rectangle. If this condition is satisfied.
              # then no overalapping rectangle.




class Solution:
    
    def doOverlap(self, l1, r1, l2, r2):
        #code here
        
        # one of the rectangle on the left side
        if ((l1[0] > r2[0]) or (l2[0] > r1[0])):
            return 0
        
        # one of the rectangle on top side
        
        if ((r1[1] > l2[1])  or (l1[1] < r2[1]) ):
            return 0
        
        return 1

if __name__ == '__main__':

    
    l1,r1 = (0,10) ,(10,0)
    l2 =(5,5) 
    r2=(15,0)
    obj = Solution()
    ans = obj.doOverlap(l1,r1,l2,r2)
    if (ans == 1):
        print("Overlapp!!")
    
    else:
        print("DO not overlap")