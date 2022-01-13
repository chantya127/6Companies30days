
# Question : Serialize and Deserialize a Binary Tree

# Input:
#       1
#     /   \
#    2     3

# Output : Generate same tree from the serialize array

# Approach : While serializing the tree , add -1 when null node is adhered.
# Follow preorder traversal for deserialize tree. When -1 is there just return None


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, arr):
    #code here
    
    if (root is None):
        arr.append(-1)
        return
    
    val = root.data
    arr.append(val)
    
    serialize(root.left,arr)
    serialize(root.right,arr)


#Function to deserialize a list and construct the tree.   
def deSerialize(arr):
    #code here
    
    def solve(ptr):
        if(ptr[0] == size):
            return (None)
        
        curr = arr[ptr[0]]
        ptr[0] +=1
        
        if (curr == -1):
            return None
        
        root = Node(curr)
        root.left = solve(ptr)
        root.right = solve(ptr)
        
        return (root)
    
    size = len(arr)
    return solve([0])

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    arr = []
    serialize(root , arr)
    new_root = deSerialize(arr)