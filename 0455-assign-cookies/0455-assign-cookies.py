class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        j = 0
        s.sort()
        g.sort()

        while(j < len(s) and i < len(g)):
            print(i,j)
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i