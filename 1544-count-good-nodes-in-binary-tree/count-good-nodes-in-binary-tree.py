# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_so_far):
            if not node:
                return 0

            good = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)

            left_good = dfs(node.left, max_so_far)
            right_good = dfs(node.right, max_so_far)

            return good + left_good + right_good

        return dfs(root, root.val)
