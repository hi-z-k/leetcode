class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        count = Counter(answers)
        for ans,freq in count.items():
            group = ans + 1
            num = (ans+freq)//group
            total += num * group
        return total
