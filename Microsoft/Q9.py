
# Question : Count Number of SubTrees having given Sum 


#Input:
# Input:
#        5
#     /    \
#   -10     3
#  /   \   /  \
#  9   8 -4    7
# X = 7
# Output: 2
# Explanation: Subtrees with sum 7 are
# [9, 8, -10] and [7] (refer the example
# in the problem description).

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

# Approach : Use postorder traversal of the tree and take left,right sum.

def countSubtreesWithSumX(root, x):
    
    def solve(node):
        if (node == None):
            return 0
        
        left = solve(node.left)
        right = solve(node.right)
        summe = node.data + left + right
        
        if (summe == x):
            ans[0] +=1
        
        return (summe)
    
    ans= [0]
    solve(root)
    return ans[0]

if __name__ == '__main__':

    root = Node(2)
    x = 1
    ans = countSubtreesWithSumX(root,x)
    print(ans)