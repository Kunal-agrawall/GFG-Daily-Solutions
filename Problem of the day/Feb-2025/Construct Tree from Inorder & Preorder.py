
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        if not inorder or not preorder:
            return None
        
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
        self.pre_index = 0
        
        def construct_tree(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = Node(root_val)
            
            root.left = construct_tree(left, inorder_index_map[root_val] - 1)
            root.right = construct_tree(inorder_index_map[root_val] + 1, right)
            
            return root
        
        return construct_tree(0, len(inorder) - 1)

    def postorderTraversal(self, root):
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.data]

#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends