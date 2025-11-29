class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
           "I" :  1,
           "V": 5,
           "X": 10,
           "L" :  50,
           "C" :  100,
           "D" :  500,
           "M" : 1000,
        }
        num = 0
        prev = 0
        for roman in s:
            curr = romanMap[roman]
            if prev < curr:
                num += (curr-2*prev)
            else:
                num += curr
            prev = curr
        return num