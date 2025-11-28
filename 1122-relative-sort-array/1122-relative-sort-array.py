class Solution:
    @staticmethod
    def builder(counter, order):
        output = []
        for place in order:
            count = counter[place]
            for _ in range(count):
                output.append(place)
        return output
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        builder = Solution.builder
        order = {key:0 for key in arr2}
        notInOrder = defaultdict(int)
        for num  in arr1:
            if num in order:
                order[num] += 1
            else:
                notInOrder[num] += 1
        inOrder = builder(order,arr2)
        arr3 = list(notInOrder.keys())
        arr3.sort()
        notOrder = builder(notInOrder,arr3)
        return inOrder + notOrder 