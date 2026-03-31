# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        paths = []
        count = 0

        def dive(node, max_val): 
            nonlocal count
            if node == None:
                return 
            if node.val >= max_val :
                count += 1
                max_val = node.val 
            dive(node.right, max_val)
            dive(node.left, max_val)
        dive(root, root.val)
        return count 