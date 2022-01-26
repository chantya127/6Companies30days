
# Question : Course Schedule II

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].


# apporach : Traverse only the courses which have o indeg .then go on reducing all the adj courses.
# finally check if all the courses has been traversed or not.

from collections import defaultdict,deque

class Solution:
    def findOrder(self, courses, pre):
        
        if (len(pre) == 0):
            
            return [i for i in range(courses)]
        
        
        indeg = [0]*(courses)
        graph  =defaultdict(list)
        ququ = deque()
        ans = []
        vis = [0]*(courses)
        
        for (adj,src) in pre:
            
            graph[src].append(adj)
            indeg[adj] +=1
        
        
        for cor in range(courses):
            
            if (indeg[cor] == 0):
                ququ.append(cor)
                
        while(ququ):
            
            node = ququ.popleft()
            ans.append(node)
            
            for adj in graph[node]:
                indeg[adj] -=1
                
                if (indeg[adj] == 0):
                    ququ.append(adj)
        
        return (ans if len(ans) == courses else [])

if __name__ == '__main__':

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    obj = Solution()
    ans = obj.findOrder(numCourses,prerequisites)
    print(ans)