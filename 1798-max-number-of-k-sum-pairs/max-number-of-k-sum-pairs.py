from collections import defaultdict

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = defaultdict(int)
        operations = 0

        for num in nums:
            complement = k - num
            if counts[complement] > 0:
                operations += 1
                counts[complement] -= 1
            else:
                counts[num] += 1

        return operations
