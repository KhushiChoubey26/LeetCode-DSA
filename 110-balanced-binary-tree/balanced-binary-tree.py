# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
         

        def get_height_imbalanced( node):
            # base condition 
            if not node:
                return 0 
            # recursively get the height of the left and right of the subtree.. if either subtree is imbalanced retunr -1
            left_height = get_height_imbalanced(node.left)
            right_height = get_height_imbalanced(node.right)
    
            if left_height == -1 or right_height == -1:
                return -1
            # if the current node's subtree is imbalanced(height diff > 1) return -1
            if abs(left_height - right_height) > 1:
                return -1 
            # return height of the current subtree
            return 1 + max(left_height, right_height)

        return get_height_imbalanced(root) != -1
        
        