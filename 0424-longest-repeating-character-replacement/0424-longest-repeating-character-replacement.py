class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        frequency = defaultdict(int)
        freq = 0
        maximum = 0
        for j in range(len(s)):
            frequency[s[j]] += 1
            freq = max(freq, frequency[s[j]])
            while ((j - i + 1) - freq) > k:
                frequency[s[i]] -= 1
                i += 1
        maximum = max(maximum, (j - i + 1)) 
        return maximum