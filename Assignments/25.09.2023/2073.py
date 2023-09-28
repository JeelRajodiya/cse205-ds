from collections import deque
from typing import List


class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        n = len(tickets)
        q = deque([i for i in range(n)])

        time = 0

        while q:
            for i in range(len(q)):

                node = q.popleft()
                tickets[node] -= 1
                if tickets[node] >= 1:
                    q.append(node)

                time += 1
                if tickets[k] == 0:
                    return time
