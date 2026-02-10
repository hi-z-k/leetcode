class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        length = 0
        for word in words:
            word_count = Counter(word)
            if word_count <= count:
                length += len(word)
        return length