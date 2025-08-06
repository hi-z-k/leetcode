class Solution:
    def isomorpic(self, s: str, t: str):
        letterMap = {}
        for i in range(len(s)):
            if s[i] in letterMap:
                if t[i] != letterMap[s[i]]:
                    return False
                continue
            else:
                letterMap[s[i]] = t[i]
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.isomorpic(s,t) and self.isomorpic(t,s)