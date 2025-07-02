from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)
        R_queue = deque()
        D_queue = deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                R_queue.append(i)
            else:
                D_queue.append(i)

        while R_queue and D_queue:
            r = R_queue.popleft()
            d = D_queue.popleft()
            if r < d:
                R_queue.append(r + n)
            else:
                D_queue.append(d + n)

        return "Radiant" if R_queue else "Dire"
