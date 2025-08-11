class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        i = 0
        j = len(s)-1
        listS = list(s)
        while(i<j):
            letterI = s[i].lower()
            letterJ = s[j].lower()
            if letterI not in VOWELS:
                i+= 1
                continue
            elif letterJ not in VOWELS:
                j-= 1
                continue
            listS[i],listS[j] = listS[j],listS[i]
            i+=1
            j-=1
        return "".join(listS)