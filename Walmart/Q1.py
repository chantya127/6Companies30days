# Question :ath with Maximum Probability

# IInput: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.


# Approach : Use dynamic programming approach and update the node only if the curr value is greater than previous one


from collections import defaultdict,deque

class Solution:
    def maxProbability(self, n, edges,prob, start, end):
        
        dp = [0.000]*(n)
        dp[start] = 1.0
        graph = defaultdict(list)
        vis = set()
        for idx in range(len(edges)):
            src ,dest = edges[idx][0] , edges[idx][1]
            wt = prob[idx]
            
            graph[src].append((dest,wt))
            graph[dest].append((src,wt))
        
        ququ = deque()
        ququ.append(start)
        
        while(ququ):
            node = ququ.popleft()
            if node == end:
                continue
                
            for adj,wt in graph[node]:
                
                if (dp[adj] < dp[node]*wt):
                    
                    dp[adj] = dp[node]*wt
                    
                    ququ.append(adj)
        
        return dp[end]

if __name__ == '__main__':

    
    n = 3; edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0; end = 2

    obj = Solution()
    
    ans = obj.maxProbability(n,edges,succProb,start,end)

    print(ans)