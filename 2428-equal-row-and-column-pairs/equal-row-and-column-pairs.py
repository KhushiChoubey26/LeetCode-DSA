from collections import Counter

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # Convert each row to a tuple and count frequency
        row_counter = Counter(tuple(row) for row in grid)
        
        count = 0
        # For each column, create tuple and check against row_counter
        for col in zip(*grid):
            count += row_counter[tuple(col)]
        
        return count
