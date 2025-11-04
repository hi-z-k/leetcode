class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        freq = [[] for _ in range(len(s)+1)]
        for char in count:
            idx = count[char]
            freq[idx].append(char*idx)
        result = []
        for i in range(len(freq)-1,-1,-1):
            if not freq[i]:
                continue
            result.extend(freq[i])
        return ''.join(result)
        