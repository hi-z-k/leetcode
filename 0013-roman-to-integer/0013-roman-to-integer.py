class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        prev = 0
        for numeral in s:
            val = roman[numeral]
            num = val
            if prev < val:
                val -= (2 * prev)
            number += val 
            prev = num    
        return number