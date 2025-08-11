class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while(i<j):
            letterI = s[i].lower()
            letterJ = s[j].lower()
            if not letterI.isalnum():
                i+= 1
                continue
            elif not letterJ.isalnum():
                j-= 1
                continue
            if letterI != letterJ:
                return False
            i+=1
            j-=1
        return True