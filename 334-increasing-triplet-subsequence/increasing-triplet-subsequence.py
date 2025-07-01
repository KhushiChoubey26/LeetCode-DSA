class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # update smallest so far
            elif num <= second:
                second = num  # update second smallest
            else:
                # num > second → found a triplet
                return True

        return False
