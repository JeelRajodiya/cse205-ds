def f(e):
    return e[1]


class Solution:

    def frequencySort(self, s: str) -> str:
        frequencyMap = {}
        for i in s:
            if i in frequencyMap:
                frequencyMap[i] += 1
            else:
                frequencyMap[i] = 1

        items = list(frequencyMap.items())
        # items = list(map(swap,items))
        items = list(sorted(items, key=f, reverse=True))

        ans = ""

        for i in items:
            ans += (i[0] * i[1])

        return ans
