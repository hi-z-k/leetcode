class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitMap = {}
        maxFruitPicked = 0
        fruitPicked = 0
        i = 0
        j = 0
        while j < len(fruits):
            fruitMap[fruits[j]] = fruitMap.get(fruits[j], 0) + 1
            fruitPicked += 1
            while len(fruitMap) > 2:
                fruitMap[fruits[i]] -= 1
                fruitPicked -= 1
                if fruitMap[fruits[i]] == 0:
                    del fruitMap[fruits[i]]
                i += 1
            maxFruitPicked = max(maxFruitPicked,fruitPicked)
            j += 1
        return maxFruitPicked