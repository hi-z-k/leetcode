class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        pattern_map = {}
        word_map = {}
        if len(pattern) != len(words):
            return False
        for p,word in zip(pattern,words):
            if p in pattern_map and pattern_map[p] != word:
                    return False
            if word in word_map and word_map[word] != p:
                    return False
            word_map[word] = p
            pattern_map[p] = word
        return True
        