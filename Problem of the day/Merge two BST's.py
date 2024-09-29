#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def merge(self, root1, root2):
        # Helper function to perform in-order traversal of BST and return a sorted list
        def inorder(root):
            stack = []
            result = []
            current = root
            while stack or current:
                while current:
                    stack.append(current)
                    current = current.left
                current = stack.pop()
                result.append(current.data)
                current = current.right
            return result

        # Merge two sorted arrays
        def merge_sorted_lists(list1, list2):
            merged_list = []
            i, j = 0, 0
            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    merged_list.append(list1[i])
                    i += 1
                else:
                    merged_list.append(list2[j])
                    j += 1
            
            # If any elements are left in either of the lists
            while i < len(list1):
                merged_list.append(list1[i])
                i += 1
            
            while j < len(list2):
                merged_list.append(list2[j])
                j += 1
                
            return merged_list
        
        # Get the sorted lists from both BSTs
        sorted_list1 = inorder(root1)
        sorted_list2 = inorder(root2)
        
        # Merge the two sorted lists and return the result
        return merge_sorted_lists(sorted_list1, sorted_list2)





#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == 'N':
        return None
    
    # Creating list of strings from input string after splitting by space
    ip = s.split()
    
    # Create the root of the tree
    root = Node(int(ip[0]))
    
    # Push the root to the queue
    queue = [root]
    
    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.pop(0)
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.left)
        
        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.right)
        i += 1
    
    return root



def main():
    t = int(input())
    for _ in range(t):
        s = input()
        root1 = buildTree(s)
        s = input()
        root2 = buildTree(s)
        obj = Solution()
        vec = obj.merge(root1, root2)
        print(" ".join(map(str, vec)))

if __name__ == "__main__":
    main()

# } Driver Code Ends