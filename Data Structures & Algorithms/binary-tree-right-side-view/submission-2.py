# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = [] 
        if root == None:
            return output

        def depth(node, level):
            if node == None:
                return 
            if len(output) == level: 
                output.append(node.val)
            depth(node.right, level + 1)
            depth(node.left, level + 1)
            
        depth(root, 0)
        return output