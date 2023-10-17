class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        cTw = {}
        wTc = {}
        for c, w in zip(pattern, words):
            if c in cTw and cTw[c] != w:
                return False
            if w in wTc and wTc[w] != c:
                return False
            cTw[c] = w
            wTc[w] = c
        return True
