class FrequencyTracker:

    def __init__(self):
        self.nums = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        nums = self.nums
        freq = self.freq

        freq[nums[number]] -= 1
        nums[number] += 1
        freq[nums[number]] += 1 
        

    def deleteOne(self, number: int) -> None:
        nums = self.nums
        freq = self.freq
        
        if nums[number]:
            freq[nums[number]] -= 1
            nums[number] -= 1
            freq[nums[number]] += 1 

        

    def hasFrequency(self, frequency: int) -> bool:
        freq = self.freq
        return freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)