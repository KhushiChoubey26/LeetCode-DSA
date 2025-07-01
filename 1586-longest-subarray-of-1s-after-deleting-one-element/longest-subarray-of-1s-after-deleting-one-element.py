class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # Shrink window if more than 1 zero
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update max length of window with at most one zero
            max_len = max(max_len, right - left + 1)

        # We must delete one element, so subtract 1
        return max_len - 1 if max_len > 0 else 0
