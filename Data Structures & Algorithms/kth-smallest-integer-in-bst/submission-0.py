# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = [] 
        def inorder(node): 
            if node == None: 
                return 
            inorder(node.left)
            output.append(node.val)
            print(output)
            inorder(node.right)
        inorder(root)
        return output[k -1]        
        