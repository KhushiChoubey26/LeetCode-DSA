# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict
        
        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            # Number of paths ending at this node with sum == targetSum
            count = prefix_sums[curr_sum - targetSum]

            # Update the current prefix sum
            prefix_sums[curr_sum] += 1

            # Continue to children
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # Backtrack: remove the current prefix sum
            prefix_sums[curr_sum] -= 1

            return count

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # To handle exact match from root
        return dfs(root, 0)
