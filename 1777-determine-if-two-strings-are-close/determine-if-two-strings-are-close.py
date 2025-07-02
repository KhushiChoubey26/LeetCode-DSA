from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # Check same length first (optional optimization)
        if len(word1) != len(word2):
            return False
        
        # 1. Must have same set of characters
        set1, set2 = set(word1), set(word2)
        if set1 != set2:
            return False

        # 2. Must have same multiset of frequencies
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        return sorted(freq1.values()) == sorted(freq2.values())
   