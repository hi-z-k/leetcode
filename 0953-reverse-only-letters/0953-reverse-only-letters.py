class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
            i = 0
            j = len(s)-1
            listS = list(s)
            while(i<j):
                letterI = s[i].lower()
                letterJ = s[j].lower()
                if not letterI.isalpha():
                    i+= 1
                    continue
                elif not letterJ.isalpha():
                    j-= 1
                    continue
                listS[i],listS[j] = listS[j],listS[i]
                i+=1
                j-=1
            return "".join(listS)