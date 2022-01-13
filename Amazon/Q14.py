
# Question : Given a binary tree and a node called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. 
# It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.


# # Input:   
#           1
#         /   \
#       2      3
#     /  \      \
#    4    5      6
#        / \      \
#       7   8      9
#                    \
#                    10


# Target Node = 8
# Output: 7
# Explanation: If leaf with the value 
# 8 is set on fire. 
# After 1 sec: 5 is set on fire.
# After 2 sec: 2, 7 are set to fire.
# After 3 sec: 4, 1 are set to fire.
# After 4 sec: 3 is set to fire.
# After 5 sec: 6 is set to fire.
# After 6 sec: 9 is set to fire.
# After 7 sec: 10 is set to fire.
# It takes 7s to burn the complete tree.


# Approach :  first Find target node to root path.
# Then take each node and calculate height ,while neglecting the previous node.


class Node:
    def __init__(self,val):
        self.left ,self.right = None, None
        self.data = val

class Solution:
    def minTime(self, root,target):
        # code here
        
        def solve(node, path , target):
            
            if (node is None):
                return False
            
            if (node.data == target):
                path.append(node)
                return True
            
            left = solve(node.left , path , target)
            if (left):
                path.append(node)
                return (True)
            
            right = solve(node.right , path ,target)
            if (right):
                path.append(node)
                return True
        
            return False
            
        def burn(node , blocker):
            if (node is None or node == blocker):
                return 0
            
            left = burn(node.left,blocker)
            right =  burn(node.right , blocker)
            
            # if (left == 0 and right ==0):
            #     return 0
            
            return max(left ,right)+1
        
        path = []
        
        solve(root , path ,target)
        
        blocker = None
        ans = 0
        time = 0
        
        for node in path:
            
            ans = max(ans , burn(node , blocker)-1 + time)
            blocker = node
            time +=1
        
        return (ans)

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    root.left.right.left = Node(7)
    root.left.right.right = Node(8)
    root.right.right.right = Node(9)

    root.right.right.right.right = Node(10)

    target = 8
    obj = Solution()
    ans = obj.minTime(root , target)
    print(ans)
