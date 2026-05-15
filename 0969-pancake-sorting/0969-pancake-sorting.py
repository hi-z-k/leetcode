class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        transformation = []
        for target in range(n, 0, -1):
            i = arr.index(target)
            if i == target - 1:
                continue
            if i != 0:
                transformation.append(i + 1)
                arr[:i+1] = arr[:i+1][::-1]
            transformation.append(target)
            arr[:target] = arr[:target][::-1]
        return transformation