class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1 = Counter(word1)
        w2 = Counter(word2)
        letters1 = set(w1.keys())
        letters2 = set(w2.keys())
        freq1 = Counter(w1.values())
        freq2 = Counter(w2.values())
        if letters1 == letters2 and freq1 == freq2:
            return True
        else:
            return False