class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # Right sum = total_sum - left_sum - current element
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num
        
        return -1
