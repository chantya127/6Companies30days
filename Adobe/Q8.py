
# Question : Given a binary tree, connect the nodes that are at same level. You'll be given an addition nextRight pointer for the same.

# Input: 

#        10                          10 ------> NULL
#       / \                       /       \
#      3   5       =>            3 ------>  5 --------> NULL
#     / \     \                /  \           \
#    4   1   2                4 --> 1 -----> 2 -------> NULL


# Approach : Do level-order traversal and connect nodes on the same level

        
#User function Template for python3
class Node:
	def __init__(self,val):
		self.data = val
		self.left = None
		self.right = None
		self.nextRight = None

from queue import deque

class Solution:
    def connect(self, root):
        
        ququ = deque()
        ququ.append(root)
        while (ququ):
            n = len(ququ)
            for i in range(n):
                curr = ququ.popleft()
                if i < n-1:
                    curr.nextRight = ququ[0]
                
                if curr.left:
                    ququ.append(curr.left)
                
                if curr.right:
                    ququ.append(curr.right)
                    
        return root	


if __name__ == '__main__':

    root = Node(4)
    obj = Solution()
    ans = obj.connect(root)
    print(ans.data)