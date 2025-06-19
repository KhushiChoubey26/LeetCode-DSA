class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        i = 0

        while i < len(nums):
            start = nums[i]
            count += 1

            # Continue this group until the difference exceeds k
            while i < len(nums) and nums[i] - start <= k:
                i += 1

        return count
