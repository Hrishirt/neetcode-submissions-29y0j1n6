# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = [] 
        if root == None:
            return []
        queue = collections.deque()

        queue.append(root)

        while len(queue) > 0:
            level = []
            for leaf in range(len(queue)):
                curr = queue.popleft() 
                level.append(curr.val)
                if curr.left != None: 
                    queue.append(curr.left)
                if curr.right != None: 
                    queue.append(curr.right)
            if len(level) > 0:
                output.append(level)
        return output