class DataStream:

    def __init__(self, value: int, k: int):
       self.value = value
       self.k = k
       self.count = defaultdict(int)
       self.stream = deque() 

    def consec(self, num: int) -> bool:
        value = self.value
        k = self.k
        count = self.count
        stream = self.stream
        if len(stream) == k:
            count[stream[0]] -= 1
            stream.popleft()
        stream.append(num)
        count[num] += 1
        if count[value] < k:
            return False
        else:
            return True


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)