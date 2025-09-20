class Solution:
    def cost(self, letter1,letter2):
        return abs(ord(letter1) - ord(letter2))
    
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        cost = 0
        maxLength = 0
        length = maxLength  
        for j in range(len(t)):
            cost += self.cost(s[j],t[j])
            length += 1
            while(cost > maxCost and i < len(t)):
                cost -= self.cost(s[i],t[i])
                i += 1
                length -= 1
            maxLength = max(maxLength,length)
        return maxLength