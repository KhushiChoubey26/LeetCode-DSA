# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0

        def dfs(node, direction, length):
            if not node:
                return
            
            self.max_len = max(self.max_len, length)

            if direction == "left":
                dfs(node.left, "right", length + 1)
                dfs(node.right, "left", 1)  # Restart from here
            else:  # direction == "right"
                dfs(node.right, "left", length + 1)
                dfs(node.left, "right", 1)  # Restart from here

        dfs(root.left, "right", 1)  # Start going left first
        dfs(root.right, "left", 1)  # Start going right first

        return self.max_len
