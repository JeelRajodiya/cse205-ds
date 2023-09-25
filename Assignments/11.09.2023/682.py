from typing import List
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.


class Solution:

    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in operations:
            if i == "D":
                scores.append(scores[-1] * 2)
            elif i == "+":
                last = scores[-2]
                last2 = scores[-1]
                scores.append(last + last2)
            elif i == "C":
                scores.pop()
            else:
                scores.append(int(i))

        return sum(scores)