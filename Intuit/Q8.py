
# Question : Number of Boomerangs

# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].


# Approach : Calculate the distance between each and every pt and store it in a hashmap.
# Suppose a distace has f freq ,meaning that f pts has same distance . So these f pts have (f-1) choices to colab.

from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        
        def find_dis(p1,p2):
            
            xval = (p2[0] - p1[0]) **2
            yval = (p2[1] - p1[1])**2
            
            return (xval + yval)
        
        size = len(points)
        ans = 0
        
        for idx in range(size):
            
            curr = points[idx]
            count = defaultdict(int)
            
            for ptr in range(size):
                
                if (idx != ptr):
                    
                    next_pt = points[ptr]
                    dis = find_dis(curr , next_pt)
                    
                    count[dis] +=1
                    
            # print(idx , count)
            for key in count:
                
                ans += (count[key] * (count[key]-1))
        
        return (ans)	


if __name__ == '__main__':

    points = [[0,0],[1,0],[2,0]]
    obj = Solution()
    ans = obj.numberOfBoomerangs(points)
    print(ans)