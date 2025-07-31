# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeaves(root):
            leaves = []

            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:
                    leaves.append(node.val)
                    return
                dfs(node.left)
                dfs(node.right)
            
            dfs(root)
            return leaves

        return getLeaves(root1) == getLeaves(root2)
