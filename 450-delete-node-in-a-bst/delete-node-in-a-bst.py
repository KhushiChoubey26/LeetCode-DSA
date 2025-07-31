# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children
            # Find the inorder successor (min in right subtree)
            min_larger_node = self.findMin(root.right)
            root.val = min_larger_node.val  # Replace value
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, min_larger_node.val)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
