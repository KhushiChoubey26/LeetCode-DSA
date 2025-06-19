# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0 
        max_width = 0
        queue = deque([(root,0)])

        while queue:
            level_size = len(queue)

            leftmost_index = queue[0][1]
            rightmost_index = leftmost_index

            for _ in range(level_size):
                node, i = queue.popleft()
                if node.left:
                    queue.append((node.left,2*i + 1))
                if node.right:
                    queue.append((node.right, 2*i + 2))
                rightmost_index = i
            max_width = max(max_width, rightmost_index - leftmost_index + 1)
        
        return max_width 
