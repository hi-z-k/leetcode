class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skillCounter = Counter(skill) 
        numPairs = len(skill)//2
        expectedSum = sum(skill)//numPairs
        chemistry = 0
        for num in skill:
            if not skillCounter[num]:
                continue
            target = expectedSum - num 
            if not skillCounter[target]:
                return -1
            skillCounter[target] -= 1
            skillCounter[num] -= 1
            chemistry += num * target 
        return chemistry

