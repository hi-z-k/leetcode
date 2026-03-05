class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_map = defaultdict(list)
        count = 0
        for i,num in enumerate(nums):
            index_map[num].append(i)
        for num, index in index_map.items():
            if len(index) == 1:
                continue
            for m,i in enumerate(index):
                for j in index[m+1:]:
                    if (i*j) % k == 0:
                        count += 1
        return count