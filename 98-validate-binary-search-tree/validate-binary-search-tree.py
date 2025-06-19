# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.is_within_bound(root, float('-inf'), float('+inf'))

    def is_within_bound(self,node,lower_bound,upper_bound):
        if not node:
            return True

        if not lower_bound < node.val < upper_bound:
            return False
        # If the left subtree isnt a BST,,, its not a BST     
        if not self.is_within_bound(node.left, lower_bound, node.val):
            return False
        # otherwise return true if right subtree is also a BST
        return self.is_within_bound(node.right, node.val, upper_bound)   