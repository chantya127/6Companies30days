# Question :Transform to Sum Tree 


# Input:
#              10
#           /      \
#         -2        6
#        /   \     /  \
#      8     -4   7    5

# Output:
#             20
#           /    \
#         4        12
#        /  \     /  \
#      0     0   0    0

# Approach : apply postorder traversal and collect left and rihgt sum and assign to current node
# then finally return to parent node

class node:

    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data


class Solution:
    def toSumTree(self, root) :
        #code here
        
        def solve(root):
            if (root is None):
                return (0)
            
            left = solve(root.left)
            right = solve(root.right)
            
            summe = left + right + root.data
            root.data = left + right
            
            return (summe)
        
        val =  solve(root)
        
        return root
        

if __name__ == '__main__':

    root= node(1)
    root.left = node(2)
    root.right = node(3)
    obj = Solution()
    ans = obj.toSumTree(root)
    
    print(ans)