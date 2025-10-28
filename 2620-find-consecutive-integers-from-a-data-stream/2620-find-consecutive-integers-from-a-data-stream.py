from collections import deque
class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.recentNotValue = -1
    def consec(self, num: int) -> bool:
        queue = self.queue
        k = self.k
        queue.append(num)
        length = len(queue)
        if num != self.value:
            self.recentNotValue = length-1
        if length < k:
            return False
        elif length > k:
            queue.popleft()
            self.recentNotValue -= 1
        return self.recentNotValue < 0


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)