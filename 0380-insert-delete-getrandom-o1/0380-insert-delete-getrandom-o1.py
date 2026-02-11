class RandomizedSet:

    def __init__(self):
        self.num_map = defaultdict(int)
        self.nums = []

    def insert(self, val: int) -> bool:
        nums = self.nums
        num_map = self.num_map
        does_not_exist = val not in num_map
        if does_not_exist:
            nums.append(val)
            num_map[val] = len(nums)-1
        return does_not_exist

    def remove(self, val: int) -> bool:
        nums = self.nums
        num_map = self.num_map
        does_exist = val in num_map
        if does_exist:
            idx = num_map[val]
            last_element = nums[-1]
            nums[idx], nums[-1] = nums[-1], nums[idx]
            num_map[last_element] = idx
            nums.pop()
            del num_map[val]
        return does_exist

    def getRandom(self) -> int:
        nums = self.nums
        return random.choice(nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()