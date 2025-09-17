class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill) - 1
        sum = skill[i] + skill[j]
        chemisty = 0
        while(i<j):
            if (skill[i] + skill[j] != sum): return -1
            chemisty += skill[i] * skill[j]
            i += 1
            j -= 1
        return chemisty

# skill => even length
# taking pairs => pair sum is equal

# [3,2,5,1,3,4] => [1,2,3,3,4,5]