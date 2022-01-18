# Question :There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites, 
# for example to do task 0 you have to first complete task 1, which is expressed as a pair:

# Input: 
# N = 4, P = 3
# prerequisites = {{1,0},{2,1},{3,2}}
# Output:
# Yes
# Explanation:
# To do task 1 you should have completed
# task 0, and to do task 2 you should 
# have finished task 1, and to do task 3 you 
# should have finished task 2. So it is possible.

# Approach :  Just check if cycle is occuring in the graph.


from collections import defaultdict


class Solution:
    def isPossible(self,n,pairs):
        #code here
        
        def solve(node):
            
            vis[node] = 1
            
            for adj in graph[node]:
                if (vis[adj] == -1):
                    val = solve(adj)
                    if (val == False):
                        return (False)
                
                elif (vis[adj] == 1):
                    return False
                    
            # whole processed
            vis[node] = 2
            return True
        
        graph = defaultdict(list)
        
        for (v,u) in pairs:
            
            graph[u].append(v)
        
        vis = [-1]*(n)
        for node in range(n):
            if(vis[node] ==-1):
                
                val = solve(node)
                if (val == False):
                    return (False)
        
        return (True)

if __name__ == '__main__':

    
    N = 4
    P = 3
    prerequisites = [[1,0],[2,1],[3,2]]
    obj = Solution()
    ans = obj.isPossible(N,prerequisites)

    print(ans)

    # done