
# Question : Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.


# Input:  N = 5, K = 4
# dict = {"baa","abcd","abca","cab","cad"}
# Output:
# 1
# Explanation:
# Here order of characters is 
# 'b', 'd', 'a', 'c' Note that words are sorted 
# and in the given language "baa" comes before 
# "abcd", therefore 'b' is before 'a' in output.
# Similarly we can find other orders.

# Approach : Traverse two words at a time and if chars are not same , then build the graph.
# then apply topo_sort on whole graph

def solve(graph , stack , node ,vis):
    
    vis[node] = 1
    for adj in graph[node]:
        if vis[adj] == 0:
            solve(graph , stack , adj , vis)
    stack.append(node)
    
    

def topo_sort(graph , k):
    vis = [0]*(k)
    stack = []
    res = ''
    for i in range(k):
        if vis[i] ==0:
            solve(graph , stack , i ,vis)
    while(stack):
        res += chr(stack.pop()+ 97)
    
    return res
    
def findOrder(dict_, n, k):
    # code here
    # return the string containing all k characters in correct order

    graph = {i:[] for i in range(k)}
    
    for i in range(n-1):
        
        word1 = dict_[i]
        word2 = dict_[i+1]
        
        for j in range(0 , min( len(word1), len(word2)) ):
            if word1[j]!=word2[j]:
                src = ord(word1[j]) - ord('a')
                dest = ord(word2[j]) - ord('a')
                graph[src].append(dest)
                break
    return topo_sort(graph,k)    

if __name__ == '__main__':

    N = 5; K = 4
    dict = ["baa","abcd","abca","cab","cad"]
    ans = findOrder(dict , N,K)
    print(ans)