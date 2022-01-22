
# Question : Given a Graph of V vertices and E edges and another edge(c - d), the task is to find if the given edge is a Bridge. i.e.,
#  removing the edge disconnects the graph.

# Input: Input: 0 -1-2-3 , c = 1, d = 2

# Output: 1
# Explanation:
# From the graph, we can clearly see that
# blocking the edge 1-2 will result in 
# disconnection of the graph. So, it is 
# a Bridge and thus the Output 1.


# Approach :Apply targans alogorithms to find all the bridges in the graph
# then check if (c,d) or (d,c) in bridges.

class Solution:
   
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, v, graph, c, d):
        # code here
        
        def solve(node, timer):
            
            disc[node] = timer[0]
            low[node] = timer[0]
            
            timer[0] +=1
            
            for adj in graph[node]:
                
                if (disc[adj] == -1):
                    
                    parent[adj] = node
                    solve(adj , timer)
                    
                    low[node] = min(low[node] , low[adj])
                    
                    if (disc[node] < low[adj]):
                        bridges.add((node ,adj))
                
                elif (adj != parent[node]):
                    low[node] = min(low[node] , disc[adj])
            
        
        low = [-1]*(v)
        disc = [-1]*(v)
        parent = [-1]*(v)
        
        bridges = set()
        timer = [0]
        
        for node in range(v):
            if (disc[node] == -1):
                solve(node , timer)
                
        if (c,d) in bridges or (d,c) in bridges:
            return 1
        
        return 0

if __name__ == '__main__':
    pass