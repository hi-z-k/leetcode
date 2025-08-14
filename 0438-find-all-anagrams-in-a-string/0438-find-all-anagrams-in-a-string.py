from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        j = len(p)
        anagramIdx = []
        countS = Counter(p)
        countP = Counter(s[:j])
        while(j <= len(s)):
            if countS == countP:
                anagramIdx.append(i)
            countP[s[i]] -= 1
            if(j<len(s)): countP[s[j]] = countP.get(s[j], 0) + 1
            i += 1
            j += 1
        return anagramIdx