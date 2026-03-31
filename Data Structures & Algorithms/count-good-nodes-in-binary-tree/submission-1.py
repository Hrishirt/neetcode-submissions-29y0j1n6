# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dive(node, max_val): 
            # nonlocal count
            if not node:
                return 0
            is_good = 1 if node.val >= max_val else 0 
            max_val = max(node.val, max_val)
            is_good += dive(node.right, max_val)
            is_good += dive(node.left, max_val)
            return is_good

        return dive(root, root.val)
          