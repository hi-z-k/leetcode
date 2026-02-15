class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        check = Counter(changed)
        original_array = []
        changed.sort()
        if len(changed) % 2 != 0:
            return []
        for num in changed:
            double = num * 2
            if num == 0 and check[num] < 2:
                continue
            if check[num] and not check[double]:
                return []
            if check[num] and check[double]:
                original_array.append(num)
                check[double] -= 1
                check[num] -= 1

        return original_array
